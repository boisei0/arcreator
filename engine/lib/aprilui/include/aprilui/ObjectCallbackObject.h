/// @file
/// @version 3.2
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://opensource.org/licenses/BSD-3-Clause
/// 
/// @section DESCRIPTION
/// 
/// Defines a callback object.

#ifndef APRILUI_CALLBACK_OBJECT_H
#define APRILUI_CALLBACK_OBJECT_H

#include <gtypes/Rectangle.h>
#include <hltypes/hstring.h>

#include "apriluiExport.h"
#include "Object.h"

namespace aprilui
{
	class apriluiExport CallbackObject : public Object
	{
	public:
		CallbackObject(chstr name, grect rect);
		~CallbackObject();
		hstr getClassName() const { return "CallbackObject"; }

		static Object* createInstance(chstr name, grect rect);

		inline void (*getDrawCallback())(CallbackObject*) { return this->drawCallback; }
		inline void setDrawCallback(void (*value)(CallbackObject*)) { this->drawCallback = value; }
		inline void setUpdateCallback(void (*value)(float)) { this->updateCallback = value; }
		
		void update(float timeDelta);
		void OnDraw();

		bool onMouseDown(april::Key keyCode);
		bool onMouseUp(april::Key keyCode);
		bool onMouseMove();
		bool onMouseScroll(float x, float y);
		void mouseCancel();

	protected:
		void (*drawCallback)(CallbackObject*);
		void (*updateCallback)(float);

	};
}

#endif