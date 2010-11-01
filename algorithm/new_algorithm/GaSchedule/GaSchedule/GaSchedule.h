// GaSchedule.h : main header file for the GaSchedule application
//
#pragma once

#ifndef __AFXWIN_H__
	#error "include 'stdafx.h' before including this file for PCH"
#endif

#include "resource.h"       // main symbols


// CGaScheduleApp:
// See GaSchedule.cpp for the implementation of this class
//

class CGaScheduleApp : public CWinApp
{
public:
	CGaScheduleApp();


// Overrides
public:
	virtual BOOL InitInstance();

// Implementation

public:
	afx_msg void OnAppAbout();
	DECLARE_MESSAGE_MAP()
};

extern CGaScheduleApp theApp;