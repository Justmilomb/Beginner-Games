#include <windows.h>

// Game creation

// Player starts at position (1,1)
int iPlayerX = 1;
int  iPlayerY = 1;

// Grid size
const int iGRIDWIDTH = 20;
const int  iGRIDHEIGHT = 20;

void DrawGame(HDC content);

// Confusing back end stuff
LRESULT CALLBACK WindowProcedure(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam)  {
	switch (uMsg) {
		case WM_DESTROY:
			PostQuitMessage(0);
			return 0;

		case WM_SIZE: {
			InvalidateRect(hwnd, NULL, TRUE);
			return 0;
		}
		
		case WM_KEYDOWN: {
			switch (wParam) {
				case VK_LEFT:
					if (iPlayerX > 0) iPlayerX--;
					break;
				case VK_RIGHT:
					if (iPlayerX < iGRIDWIDTH - 1) iPlayerX++;
					break;
				case VK_UP:
					if (iPlayerY > 0) iPlayerY--;
					break;
				case VK_DOWN:
					if (iPlayerY < iGRIDHEIGHT - 1) iPlayerY++;
					break;
			}
			InvalidateRect(hwnd, NULL, TRUE); // Forces a redraw
			return 0;
		}

		case WM_PAINT: {

			PAINTSTRUCT ps;
			HDC hdc = BeginPaint(hwnd, &ps);
			DrawGame(hdc);
			EndPaint(hwnd, &ps);
			return 0;
		}

		default:
			return DefWindowProc(hwnd, uMsg, wParam, lParam);

	}
}

void DrawGame(HDC content) {
	// Clearing area thats just changed
	RECT Rectangle;
	GetClipBox(content, &Rectangle);
	HBRUSH hBrush = (HBRUSH)GetStockObject(WHITE_BRUSH);
	FillRect(content, &Rectangle, hBrush);
	GetClientRect(WindowFromDC(content), &Rectangle);

	int iWindowWidth = Rectangle.right;
	int iWindowHeight = Rectangle.bottom;

	int iCellWidth = iWindowWidth / iGRIDWIDTH;
	int iCellHeight = iWindowHeight / iGRIDHEIGHT;



	for (int y = 0; y < iGRIDHEIGHT; y++) {
		for (int x = 0; x < iGRIDWIDTH; x++) {
			wchar_t Background = L'.';

			if (x == iPlayerX && y == iPlayerY) {
				Background = L'@';
			}
			wchar_t szDrawing[2] = {Background, 0 }; // Create a string due to TextOutW needing string not characters and 0 is the terminator of a string
			TextOutW(content, x * iCellWidth, y * iCellHeight, szDrawing, 1); // Each pixel location scaled up for even spacing
		}

	}
}

// Create window
int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) {

	WNDCLASS wc = { 0 };
	wc.lpfnWndProc = WindowProcedure;
	wc.hInstance = hInstance;
	wc.lpszClassName = L"Main Window";

	RegisterClass(&wc);
	
		// Wide string format unicode
	LPCWSTR lpText = L"Main Window";
	LPCWSTR lpTitle = L"My window";

	HWND hwnd = CreateWindowEx(
		0,
		lpText,
		lpTitle,
		WS_OVERLAPPEDWINDOW,
		CW_USEDEFAULT,
		CW_USEDEFAULT,
		800,
		600,
		NULL,
		NULL,
		hInstance,
		NULL
	);

	if (hwnd == NULL) {
		MessageBox(NULL, L"Failed to create window!", L"Error", MB_OK);
		return 0;
	}

	ShowWindow(hwnd, nCmdShow);

	UpdateWindow(hwnd);

	MSG msg = { 0 };
	while (GetMessage(&msg, NULL, 0, 0)) {
		TranslateMessage(&msg);
		DispatchMessage(&msg);
	}


	return (int)msg.wParam;
}