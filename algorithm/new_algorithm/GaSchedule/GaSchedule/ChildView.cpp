// ChildView.cpp : implementation of the CChildView class
//

#include "stdafx.h"
#include "GaSchedule.h"
#include "ChildView.h"

#include "Algorithm\Configuration.h"
#include "Algorithm\Room.h"
#include "Algorithm\Schedule.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

CChildView::CChildView() : _schedule(NULL),
	_running(false)
{
	Algorithm::GetInstance().GetObserver()->SetWindow( this );
}

CChildView::~CChildView()
{
	if( _schedule )
		delete _schedule;
}

void CChildView::SetSchedule(const Schedule* schedule)
{
	CSingleLock lock( &_sect, TRUE );

	if( _schedule )
		delete _schedule;

	_schedule = schedule->MakeCopy( false );

	lock.Unlock();

	Invalidate();
}

void CChildView::SetNewState(AlgorithmState state)
{
	_running = state == AS_RUNNING;
}

BEGIN_MESSAGE_MAP(CChildView, CWnd)
	ON_WM_PAINT()
	ON_COMMAND(ID_FILE_START, &CChildView::OnFileStart)
	ON_COMMAND(ID_FILE_STOP, &CChildView::OnFileStop)
	ON_COMMAND(ID_FILE_OPEN_CONFIGURATION, &CChildView::OnFileOpenConfiguration)
	ON_WM_ERASEBKGND()
	ON_WM_HSCROLL()
	ON_WM_VSCROLL()
	ON_WM_SIZE()
	ON_WM_MOUSEWHEEL()
	ON_WM_CLOSE()
	ON_UPDATE_COMMAND_UI(ID_FILE_OPEN_CONFIGURATION, &CChildView::OnUpdateFileOpenConfiguration)
	ON_UPDATE_COMMAND_UI(ID_FILE_START, &CChildView::OnUpdateFileStart)
	ON_UPDATE_COMMAND_UI(ID_FILE_STOP, &CChildView::OnUpdateFileStop)
END_MESSAGE_MAP()

// CChildView message handlers

BOOL CChildView::PreCreateWindow(CREATESTRUCT& cs) 
{
	if (!CWnd::PreCreateWindow(cs))
		return FALSE;

	cs.dwExStyle |= WS_EX_CLIENTEDGE;
	cs.style &= ~WS_BORDER;
	cs.lpszClass = AfxRegisterWndClass(CS_HREDRAW|CS_VREDRAW|CS_DBLCLKS, 
		::LoadCursor(NULL, IDC_ARROW), reinterpret_cast<HBRUSH>(COLOR_WINDOW+1), NULL);

	return TRUE;
}

const int ROOM_CELL_WIDTH = 85;
const int ROOM_CELL_HEIGHT = 50;

const int ROOM_MARGIN_WIDTH = 50;
const int ROOM_MARGIN_HEIGHT = 50;

const int ROOM_COLUMN_NUMBER = DAYS_NUM + 1;
const int ROOM_ROW_NUMBER = DAY_HOURS + 1;

const int ROOM_TABLE_WIDTH = ROOM_CELL_WIDTH * ROOM_COLUMN_NUMBER + ROOM_MARGIN_WIDTH;
const int ROOM_TABLE_HEIGHT = ROOM_CELL_HEIGHT * ROOM_ROW_NUMBER + ROOM_MARGIN_HEIGHT;

void CChildView::OnPaint() 
{
	CPaintDC wndDC(this);

	CRect clientRect;
	GetClientRect( clientRect );

	CDC dc;
	CBitmap bmp;
	dc.CreateCompatibleDC( &wndDC );
	bmp.CreateCompatibleBitmap( &wndDC, clientRect.Width(), clientRect.Height() );
	dc.SelectObject( &bmp );

	int sx = -GetScrollPos( SB_HORZ );
	int sy = -GetScrollPos( SB_VERT );

	CBrush bgBrush( RGB( 255, 255, 255 ) );
	dc.FillRect( clientRect, &bgBrush );

	dc.SetBkColor( RGB( 255, 255, 255 ) );
	dc.SetBkMode( TRANSPARENT );

	CFont tableHeadersFont;
	tableHeadersFont.CreateFont( 24, 0, 0, 0, 700, FALSE, FALSE, FALSE, DEFAULT_CHARSET,
		OUT_DEFAULT_PRECIS, CLIP_DEFAULT_PRECIS, DEFAULT_QUALITY, DEFAULT_PITCH | FF_DONTCARE,
		"Arial" );

	CFont tableTextFont;
	tableTextFont.CreateFont( 14, 0, 0, 0, 100, FALSE, FALSE, FALSE, DEFAULT_CHARSET,
		OUT_DEFAULT_PRECIS, CLIP_DEFAULT_PRECIS, DEFAULT_QUALITY, DEFAULT_PITCH | FF_DONTCARE,
		"Arial" );

	CFont roomDescFont;
	roomDescFont.CreateFont( 12, 0, 0, 0, 100, FALSE, FALSE, FALSE, DEFAULT_CHARSET,
		OUT_DEFAULT_PRECIS, CLIP_DEFAULT_PRECIS, DEFAULT_QUALITY, DEFAULT_PITCH | FF_DONTCARE,
		"Arial" );

	CFont criteriaFont;
	criteriaFont.CreateFont( 14, 0, 0, 0, 900, FALSE, FALSE, FALSE, DEFAULT_CHARSET,
		OUT_DEFAULT_PRECIS, CLIP_DEFAULT_PRECIS, DEFAULT_QUALITY, DEFAULT_PITCH | FF_DONTCARE,
		"Arial" );

	CBrush classBrush( RGB( 255, 255, 245 ) );
	CBrush overlapBrush( HS_BDIAGONAL, RGB( 255, 0, 0 ) );
	CPen overlapPen( PS_NULL, 1, RGB( 255, 0, 0 ) );

	int nr = Configuration::GetInstance().GetNumberOfRooms();
	for( int k = 0; k < nr; k++ )
	{
		for( int i = 0; i < ROOM_COLUMN_NUMBER; i++ )
		{
			for( int j = 0; j < ROOM_ROW_NUMBER; j++ )
			{
				int l = k % 2;
				int m = k / 2;

				CRect rect( 
					sx + ROOM_TABLE_WIDTH * l + ROOM_MARGIN_WIDTH + i * ROOM_CELL_WIDTH - 1,
					sy + ROOM_TABLE_HEIGHT * m + ROOM_MARGIN_HEIGHT + j * ROOM_CELL_HEIGHT - 1,
					sx + ROOM_TABLE_WIDTH * l + ROOM_MARGIN_WIDTH + ( i + 1 ) * ROOM_CELL_WIDTH,
					sy + ROOM_TABLE_HEIGHT * m + ROOM_MARGIN_HEIGHT + ( j + 1 ) * ROOM_CELL_HEIGHT );

				if( i == 0 || j == 0 )
					dc.Rectangle( rect );

				if( i == 0 && j == 0 )
				{
					dc.SelectObject( &roomDescFont );

					rect.bottom -= rect.Height() / 2;
					dc.Rectangle( rect );

					CString str;
					str.Format( "Room: %s", Configuration::GetInstance().GetRoomById( k )->GetName().c_str() );
					dc.DrawText( str, rect, DT_CENTER | DT_VCENTER | DT_SINGLELINE );

					rect.MoveToY( rect.bottom - 1 );

					rect.right -= rect.Width() / 2 + 7;
					dc.Rectangle( rect );

					str.Format( "Lab: %c", Configuration::GetInstance().GetRoomById( k )->IsLab() ? 'Y' : 'N' );
					dc.DrawText( str, rect, DT_CENTER | DT_VCENTER | DT_SINGLELINE );

					rect.MoveToX( rect.right - 1 );
					rect.right += 14;

					str.Format( "Seats: %d", Configuration::GetInstance().GetRoomById( k )->GetNumberOfSeats() );
					dc.DrawText( str, rect, DT_CENTER | DT_VCENTER | DT_SINGLELINE );
				}

				dc.SelectObject( &tableHeadersFont );

				if( i == 0 && j > 0 )
				{
					CString str;
					str.Format( "%d - %d", 9 + j - 1, 9 + j );

					dc.DrawText( str, rect, DT_CENTER | DT_VCENTER | DT_SINGLELINE );
				}

				if( j == 0 && i > 0 )
				{
					static const char* days[] = { "MON", "THU", "WED", "THR", "FRI" };

					dc.DrawText( days[ i - 1 ], 3, rect, DT_CENTER | DT_VCENTER | DT_SINGLELINE );
				}
			}
		}
	}

	dc.SelectObject( &classBrush );

	CSingleLock lock( &_sect, TRUE );

	if( _schedule )
	{
		CString fit;
		fit.Format( "Fitness: %f, Generation: %d", _schedule->GetFitness(),
			Algorithm::GetInstance().GetCurrentGeneration() );

		dc.SelectObject( &tableHeadersFont );

		dc.TextOutA( sx + 10, sy + 10, fit );

		const hash_map<CourseClass*, int>& classes = _schedule->GetClasses();
		int ci = 0;
		for( hash_map<CourseClass*, int>::const_iterator it= classes.begin(); it != classes.end(); ++it, ci += 5 )
		{
			CourseClass* c = ( *it ).first;
			int p = ( *it ).second;

			int t = p % ( nr * DAY_HOURS );
			int d = p / ( nr * DAY_HOURS ) + 1;
			int r = t / DAY_HOURS;
			t = t % DAY_HOURS + 1;

			int l = r % 2;
			int m = r / 2;

			CRect rect( 
				sx + ROOM_TABLE_WIDTH * l + ROOM_MARGIN_WIDTH + d * ROOM_CELL_WIDTH - 1,
				sy + ROOM_TABLE_HEIGHT * m + ROOM_MARGIN_HEIGHT + t * ROOM_CELL_HEIGHT - 1,
				sx + ROOM_TABLE_WIDTH * l + ROOM_MARGIN_WIDTH + ( d + 1 ) * ROOM_CELL_WIDTH,
				sy + ROOM_TABLE_HEIGHT * m + ROOM_MARGIN_HEIGHT + ( t + c->GetDuration() ) * ROOM_CELL_HEIGHT );

			dc.Rectangle( rect );

			CString str;
			str.Format( "%s\n%s\n/", c->GetCourse().GetName().c_str(), c->GetProfessor().GetName().c_str() );

			for( list<StudentsGroup*>::const_iterator it = c->GetGroups().begin(); 
				it != c->GetGroups().end(); ++it )
			{
				str += ( *it )->GetName().c_str();
				str += "/";
			}

			if( c->IsLabRequired() )
				str += "\nLab";

			rect.top += 5;
			rect.bottom -= 5;
			rect.left += 5;
			rect.right -= 5;

			dc.SelectObject( &tableTextFont );
			
			dc.DrawText( str, rect, DT_CENTER | DT_WORDBREAK );

			dc.SelectObject( &criteriaFont );

			dc.SetTextColor( _schedule->GetCriteria()[ ci + 0 ] ? RGB( 49, 147, 120 ) : RGB( 206, 0, 0 ) );
			dc.TextOut( rect.left, rect.bottom - 10, "R", 1 );
			dc.SetTextColor( _schedule->GetCriteria()[ ci + 1 ] ? RGB( 49, 147, 120 ) : RGB( 206, 0, 0 ) );
			dc.TextOut( rect.left + 10, rect.bottom - 10, "S", 1 );
			dc.SetTextColor( _schedule->GetCriteria()[ ci + 2 ] ? RGB( 49, 147, 120 ) : RGB( 206, 0, 0 ) );
			dc.TextOut( rect.left + 20, rect.bottom - 10, "L", 1 );
			dc.SetTextColor( _schedule->GetCriteria()[ ci + 3 ] ? RGB( 49, 147, 120 ) : RGB( 206, 0, 0 ) );
			dc.TextOut( rect.left + 30, rect.bottom - 10, "P", 1 );
			dc.SetTextColor( _schedule->GetCriteria()[ ci + 4 ] ? RGB( 49, 147, 120 ) : RGB( 206, 0, 0 ) );
			dc.TextOut( rect.left + 40, rect.bottom - 10, "G", 1 );

			dc.SetTextColor( RGB( 0, 0, 0 ) );
		}

		dc.SelectObject( &overlapPen );
		dc.SelectObject( &overlapBrush );

		int i = 0;
		for( vector<list<CourseClass*>>::const_iterator it = _schedule->GetSlots().begin();
			it != _schedule->GetSlots().end(); ++it, ++i )
		{
			if( ( *it ).size() > 1 )
			{
				int t = i % ( nr * DAY_HOURS );
				int d = i / ( nr * DAY_HOURS ) + 1;
				int r = t / DAY_HOURS;
				t = t % DAY_HOURS + 1;

				int l = r % 2;
				int m = r / 2;

				CRect rect( 
					sx + ROOM_TABLE_WIDTH * l + ROOM_MARGIN_WIDTH + d * ROOM_CELL_WIDTH - 1,
					sy + ROOM_TABLE_HEIGHT * m + ROOM_MARGIN_HEIGHT + t * ROOM_CELL_HEIGHT - 1,
					sx + ROOM_TABLE_WIDTH * l + ROOM_MARGIN_WIDTH + ( d + 1 ) * ROOM_CELL_WIDTH,
					sy + ROOM_TABLE_HEIGHT * m + ROOM_MARGIN_HEIGHT + ( t + 1 ) * ROOM_CELL_HEIGHT );

				dc.Rectangle( rect );
			}
		}
	}

	lock.Unlock();

	wndDC.BitBlt( 0, 0, clientRect.Width(), clientRect.Height(), &dc, 0, 0, SRCCOPY );
}

DWORD WINAPI StartAlg(LPVOID param)
{
	Algorithm::GetInstance().Start();
	return 0;
}

void CChildView::OnFileStart()
{
	DWORD tid;
	HANDLE thread = CreateThread( NULL, 0, StartAlg, NULL, 0, &tid );
	CloseHandle( thread );
}

void CChildView::OnFileStop()
{
	Algorithm::GetInstance().Stop();
}

void CChildView::OnFileOpenConfiguration()
{
	CFileDialog dlg( TRUE, NULL, NULL, 0, 
		"Class Schedule Config Files (*.cfg)|*.cfg|All Files (*.*)|*.*|", this );

	if( dlg.DoModal() == IDOK )
	{
		Configuration::GetInstance().ParseFile( dlg.GetFileName().GetBuffer() );

		ComputeScrollBars();
		Invalidate();
	}
}

BOOL CChildView::OnEraseBkgnd(CDC* pDC)
{
	return false;
}

void CChildView::ComputeScrollBars()
{
	int nr = Configuration::GetInstance().GetNumberOfRooms();

	int w = ROOM_TABLE_WIDTH;
	if( nr == 0 )
		w = 0;
	else if( nr > 1 )
		w *= 2;

	int h = ( ( nr / 2 ) + nr % 2 ) * ROOM_TABLE_HEIGHT;

	w += ROOM_MARGIN_WIDTH;
	h += ROOM_MARGIN_HEIGHT;

	CRect cr;
	GetClientRect( cr );

	SCROLLINFO hsi;
	hsi.cbSize = sizeof( hsi );
	hsi.fMask = SIF_RANGE | SIF_PAGE;
	hsi.nMin = 0;
	hsi.nMax = w;
	hsi.nPage = cr.Width();

	SetScrollInfo( SB_HORZ, &hsi, TRUE );

	hsi.nMax = h;
	hsi.nPage = cr.Height();

	SetScrollInfo( SB_VERT, &hsi, TRUE );
}

void CChildView::Scroll(int scrollBar, int nSBCode, int nPos)
{
	int minpos, maxpos, curpos;

	GetScrollRange( SB_HORZ, &minpos, &maxpos ); 
	maxpos = GetScrollLimit( scrollBar );
	curpos = GetScrollPos( scrollBar );

	switch( nSBCode )
	{
	case SB_LEFT:
		curpos = minpos;
		break;

	case SB_RIGHT:
		curpos = maxpos;
		break;

	case SB_ENDSCROLL:
		break;

	case SB_LINELEFT:
		if( curpos > minpos )
			curpos--;
		break;

	case SB_LINERIGHT:
		if( curpos < maxpos )
			curpos++;
		break;

	case SB_PAGELEFT:
		{
			SCROLLINFO   info;
			GetScrollInfo( scrollBar, &info, SIF_ALL);

			if( curpos > minpos )
				curpos = max(minpos, curpos - (int) info.nPage);
		}
		break;

	case SB_PAGERIGHT:
		{
			SCROLLINFO info;
			GetScrollInfo( scrollBar, &info, SIF_ALL);

			if( curpos < maxpos )
				curpos = min( maxpos, curpos + (int)info.nPage );
		}
		break;

	case SB_THUMBPOSITION:
		curpos = nPos;
		break;

	case SB_THUMBTRACK:
		curpos = nPos;
		break;
	}

	SetScrollPos( scrollBar, curpos);
}

void CChildView::OnHScroll(UINT nSBCode, UINT nPos, CScrollBar* pScrollBar)
{
	Scroll( SB_HORZ, nSBCode, nPos );
	Invalidate();
	
	CWnd::OnHScroll(nSBCode, nPos, pScrollBar);
}

void CChildView::OnVScroll(UINT nSBCode, UINT nPos, CScrollBar* pScrollBar)
{
	Scroll( SB_VERT, nSBCode, nPos );
	Invalidate();

	CWnd::OnVScroll(nSBCode, nPos, pScrollBar);
}

void CChildView::OnSize(UINT nType, int cx, int cy)
{
	CWnd::OnSize(nType, cx, cy);

	ComputeScrollBars();
}

BOOL CChildView::OnMouseWheel(UINT nFlags, short zDelta, CPoint pt)
{
	SetScrollPos( SB_VERT, GetScrollPos( SB_VERT ) - zDelta );
	Invalidate();

	return CWnd::OnMouseWheel(nFlags, zDelta, pt);
}

void CChildView::OnClose()
{
	Algorithm::GetInstance().Stop();
	Algorithm::GetInstance().GetObserver()->WaitEvent();
	Algorithm::FreeInstance();

	CWnd::OnClose();
}

void CChildView::OnUpdateFileOpenConfiguration(CCmdUI *pCmdUI)
{
	pCmdUI->Enable( !_running );
}

void CChildView::OnUpdateFileStart(CCmdUI *pCmdUI)
{
	pCmdUI->Enable( !_running && !Configuration::GetInstance().IsEmpty() );
}

void CChildView::OnUpdateFileStop(CCmdUI *pCmdUI)
{
	pCmdUI->Enable( _running );
}
