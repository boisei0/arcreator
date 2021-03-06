/// @file
/// @version 3.2
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://opensource.org/licenses/BSD-3-Clause

#include "MemberCallbackEvent.h"

namespace aprilui
{
	MemberCallbackEvent::~MemberCallbackEvent()
	{
		delete this->callback;
	}

	void MemberCallbackEvent::execute(void* params)
	{
		this->callback->execute((EventArgs*)params);
	}

}
