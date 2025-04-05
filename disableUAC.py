import winreg
import ctypes

def is_admin():
    """Verifica se o script está com permissões elevadas"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    exit()
try:
    chave = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"

    reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, chave, 0, winreg.KEY_SET_VALUE)

    # Escrever valor 0 (desativa UAC)
    winreg.SetValueEx(reg_key, "EnableLUA", 0, winreg.REG_DWORD, 0)
    winreg.CloseKey(reg_key)

    print("✅ Valor 'EnableLUA' alterado com sucesso")
except PermissionError:
    print("❌ Permissão negada. Execute o script como administrador.")
except Exception as e:
    print(f"Erro ao modificar o registro: {e}")