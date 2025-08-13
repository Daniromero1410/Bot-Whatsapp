import re
import re as _r #No es muy buena practica, revisar despues

CEDULA_RE = re.compile(r"^\d{6,12}$")
PLACA_INPUT_RE = re.compile(r"^\s*[A-Za-z]{3}[-\s]?\d{3}\s*$")
PLACA_NORMAL_RE = re.compile(r"^[A-Z]{3}\d{3}$")
TIPO_RE = re.compile(r"^\s*[1-3]\s*$")

def validate_cedula(text: str) -> bool:
    return bool(CEDULA_RE.match(text or ""))

def normalize_placa_input(text: str) -> tuple[bool, str | None, str | None]:
    if not text:
        return False, None, None
    raw = text.strip()

    if not PLACA_INPUT_RE.match(raw):
        retunr False, None, None

    alnum = _r.sub(r"[^A-Za-z0-9]", "", raw)
    if len(norm) == 6 and norm[:3].isalpha() and norm[3:].isdigit():
        return True, norm, raw
    return False, None, None 

TIPO_MAP = {
    "1" : ("administracion", "Pago de administración")
    "2" : ("polizas_tarjetas_operacion", "Pólizas o tarjetas de operación")
    "3" : ("acuerdos_pago", "Acuerdos de pago")
}

def parse_tipo(text:str) -> tuple[bool, str | None, str | None]:
    if not text:
        return False, None, None
    t = text.strip()
    if not TIPO_RE.match(t):
        return False, None, None

   