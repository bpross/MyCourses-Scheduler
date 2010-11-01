
class Schedule;
enum AlgorithmState;

#pragma once

class CChildView : public CWnd
{

public:

	CChildView();

	virtual ~CChildView();

private:

	CCriticalSection _sect;

	Schedule* _schedule;

	bool _running;

public:

	void SetSchedule(const Schedule* schedule);

	void SetNewState(AlgorithmState state);

private:

	void ComputeScrollBars();

	void Scroll(int scrollBar, int nSBCode, int nPos);

protected:

	virtual BOOL PreCreateWindow(CREATESTRUCT& cs);

protected:

	afx_msg void OnPaint();
	DECLARE_MESSAGE_MAP()

public:

	afx_msg void OnFileStart();
	afx_msg void OnFileStop();
	afx_msg void OnFileOpenConfiguration();
	afx_msg BOOL OnEraseBkgnd(CDC* pDC);
	afx_msg void OnHScroll(UINT nSBCode, UINT nPos, CScrollBar* pScrollBar);
	afx_msg void OnVScroll(UINT nSBCode, UINT nPos, CScrollBar* pScrollBar);
	afx_msg void OnSize(UINT nType, int cx, int cy);
	afx_msg BOOL OnMouseWheel(UINT nFlags, short zDelta, CPoint pt);
	afx_msg void OnClose();
	afx_msg void OnUpdateFileOpenConfiguration(CCmdUI *pCmdUI);
	afx_msg void OnUpdateFileStart(CCmdUI *pCmdUI);
	afx_msg void OnUpdateFileStop(CCmdUI *pCmdUI);
};

