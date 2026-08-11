import os
import sys

# buffer para almacenar un carácter "empujado" cuando se detecta durante la lectura de un número
_pushed_char = None


def limpiar_terminal():
    # Detectar plataforma
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def operacion_anterior(memoria):
    for i in memoria:
        print(i, end="")


# Función cross-platform para leer un carácter sin esperar Enter
def _getch():
    try:
        import msvcrt
        ch = msvcrt.getwch()
        return ch
    except ImportError:
        import tty
        import termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
            return ch
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)


def leer_numero_sin_enter(prompt=""):
    """Lee un número digitado sin necesidad de presionar Enter.

    Si el usuario presiona una operación (+-*/^%! o =), la función devuelve
    el número leído hasta ese momento y almacena el operador en un buffer
    interno para que la siguiente llamada a leer_operacion_sin_enter lo recoja
    inmediatamente.
    """
    global _pushed_char
    buf = ""
    sys.stdout.write(prompt)
    sys.stdout.flush()

    operators = set("+-*/^!%=")

    while True:
        ch = _getch()
        # Ctrl-C
        if ch == "\x03":
            raise KeyboardInterrupt

        # dígitos o punto decimal
        if ch.isdigit() or ch == ".":
            # evitar múltiples puntos
            if ch == "." and "." in buf:
                continue
            buf += ch
            sys.stdout.write(ch)
            sys.stdout.flush()
            continue

        # backspace (Windows '\b' o POSIX '\x7f')
        if ch in ("\x08", "\x7f"):
            if buf:
                buf = buf[:-1]
                sys.stdout.write("\b \b")
                sys.stdout.flush()
            continue

        # operador: guardar en buffer y salir devolviendo número
        if ch in operators:
            _pushed_char = ch
            # mostrar el operador (para mantener consistencia visual)
            sys.stdout.write(ch)
            sys.stdout.flush()
            break

        # Enter también termina la lectura
        if ch in ("\r", "\n"):
            break

        # ignorar otros caracteres
        continue

    # si el buffer está vacío, asumimos 0
    if buf == "" or buf == ".":
        return 0

    # devolver número como int si es entero, sino float
    if "." in buf:
        return float(buf)
    else:
        return int(buf)


def leer_operacion_sin_enter(prompt=""):
    """Devuelve el siguiente operador. Si un operador fue presionado al terminar
    la lectura de un número, lo devuelve inmediatamente.
    """
    global _pushed_char
    if _pushed_char is not None:
        ch = _pushed_char
        _pushed_char = None
        return ch

    sys.stdout.write(prompt)
    sys.stdout.flush()

    operators = set(["+", "-", "*", "/", "^", "!", "%", "=", "L"])  # 'L' para "Log" si se usa

    while True:
        ch = _getch()
        # Ctrl-C
        if ch == "\x03":
            raise KeyboardInterrupt

        # aceptar secuencias como 'Log' (si el usuario escribe L luego o)
        if ch.upper() == "L":
            # intentar leer el resto para formar "Log" (no requiere Enter)
            # leemos los siguientes dos caracteres si existen
            rest = ""
            # leer 'o' y 'g' si el usuario los teclea inmediatamente
            for _ in range(2):
                ch2 = _getch()
                rest += ch2
                sys.stdout.write(ch2)
                sys.stdout.flush()
            token = ch + rest
            if token == "Log":
                return "Log"
            # si no es Log, continuar el loop (aunque improbable)

        if ch in operators:
            sys.stdout.write(ch)
            sys.stdout.flush()
            return ch

        # ignorar otros caracteres
        continue
