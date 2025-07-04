import ctypes
import ctypes.wintypes as wintypes

# Basic constants
USER32 = ctypes.windll.user32
KERNEL32 = ctypes.windll.kernel32
GDI32 = ctypes.windll.gdi32

# Window message constants
WM_DESTROY = 0x0002
WM_PAINT = 0x000F
WM_CLOSE = 0x0010

# Define windows procedure
HCURSOR = wintypes.HANDLE
WNDPROC = ctypes.WINFUNCTYPE(ctypes.c_long, wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM)
def WindowsProcedure(hwnd, msg, wParam, lParam):
    if msg == WM_DESTROY:
        USER32.PostQuitMessage(0)
        return 0 
    return USER32.DefWindowProcW(hwnd, msg, wParam, ctypes.c_long(lParam))

WndProcCallBack = WNDPROC(WindowsProcedure)

class WNDCLASS(ctypes.Structure):
    _fields_ = [("Style", wintypes.UINT), ("lpfnWndProc", WNDPROC), ("cbClsExtra", ctypes.c_int), ("cbWndExtra", ctypes.c_int), ("hInstance", wintypes.HINSTANCE), ("hIcon", wintypes.HICON),
                ("hCursor", HCURSOR), ("hbrBackground", wintypes.HBRUSH), ("lpszMenuName", wintypes.LPCWSTR), ("lpszClassName", wintypes.LPCWSTR)]
    
wndclass = WNDCLASS()
wndclass.style = 0
wndclass.lpfnWndProc = WndProcCallBack
wndclass.cbClsExtra = 0
wndclass.cbWndExtra = 0
wndclass.hInstance = KERNEL32.GetModuleHandleW(None)
wndclass.hIcon = None
wndclass.hCursor = USER32.LoadCursorW(None, 32512)
wndclass.hbrBackground = 6
wndclass.lpszMenuName = "Hello"
wndclass.lpszClassName = "Bum"

atom = USER32.RegisterClassW(ctypes.byref(wndclass))
if not atom:
    raise ctypes.WinError()

hwnd = USER32.CreateWindowExW(
    0, wndclass.lpszClassName, "First Window",
    0xcf0000, 100, 100, 800, 600, None, None, wndclass.hInstance, None
)

USER32.ShowWindow(hwnd, 1)
USER32.UpdateWindow(hwnd)

msg = wintypes.MSG()
while USER32.GetMessageW(ctypes.byref(msg), 0, 0, 0) != 0:
    USER32.TranslateMessage(ctypes.byref(msg))
    USER32.DispatchMessageW(ctypes.byref(msg))