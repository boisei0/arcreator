/// @file
/// @version 3.2
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://opensource.org/licenses/BSD-3-Clause

#include <gtypes/Rectangle.h>
#include <gtypes/Vector2.h>
#include <hltypes/hstring.h>

#include "aprilui.h"
#include "Dataset.h"
#include "ObjectLabel.h"

namespace aprilui
{
	Label::Label(chstr name, grect rect) : Object(name, rect), LabelBase()
	{
		this->text = "Label: " + name;
	}

	Label::~Label()
	{
	}

	Object* Label::createInstance(chstr name, grect rect)
	{
		return new Label(name, rect);
	}

	Dataset* Label::getDataset()
	{
		return Object::getDataset();
	}

	harray<PropertyDescription> Label::getPropertyDescriptions()
	{
		return (Object::getPropertyDescriptions() + LabelBase::getPropertyDescriptions());
	}

	void Label::OnDraw()
	{
		Object::OnDraw();
		float disabledAlphaFactor = this->_getDisabledAlphaFactor();
		april::Color color = this->_getDrawColor();
		color.a = (unsigned char)(color.a * disabledAlphaFactor);
		april::Color backgroundColor = this->backgroundColor;
		backgroundColor.a = (unsigned char)(backgroundColor.a * disabledAlphaFactor);
		LabelBase::_drawLabel(this->_getDrawRect(), color, backgroundColor);
	}

	void Label::notifyEvent(chstr name, void* params)
	{
		Object::notifyEvent(name, params);
		LabelBase::notifyEvent(name, params);
	}

	bool Label::triggerEvent(chstr name, april::Key keyCode, chstr extra)
	{
		return Object::triggerEvent(name, keyCode, extra);
	}

	bool Label::triggerEvent(chstr name, april::Button buttonCode, chstr extra)
	{
		return Object::triggerEvent(name, buttonCode, extra);
	}

	bool Label::triggerEvent(chstr name, float x, float y, april::Key keyCode, chstr extra)
	{
		return Object::triggerEvent(name, x, y, keyCode, extra);
	}

	bool Label::onMouseDown(april::Key keyCode)
	{
		if (Object::onMouseDown(keyCode))
		{
			return true;
		}
		if (isCursorInside())
		{
			this->triggerEvent("MouseDown", keyCode);
			return true;
		}
		return false;
	}
	
	bool Label::onMouseUp(april::Key keyCode)
	{
		if (Object::onMouseUp(keyCode))
		{
			return true;
		}
		if (this->isCursorInside())
		{
			// TODO - this is not good as it will happen if you didn't click on the label, but released the button over it
			this->triggerEvent("Click", keyCode);
			return true;
		}
		return false;
	}
	
	hstr Label::getProperty(chstr name)
	{
		hstr result = Object::getProperty(name);
		if (result == "")
		{
			result = LabelBase::getProperty(name);
		}
		return result;
	}

	bool Label::setProperty(chstr name, chstr value)
	{
		if (Object::setProperty(name, value))
		{
			return true;
		}
		return LabelBase::setProperty(name, value);
	}
	
}
