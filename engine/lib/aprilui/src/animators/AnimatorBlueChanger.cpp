/// @file
/// @version 3.2
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://opensource.org/licenses/BSD-3-Clause

#include <hltypes/hstring.h>

#include "AnimatorBlueChanger.h"

namespace aprilui
{
	namespace Animators
	{
		BlueChanger::BlueChanger(chstr name) : Animator(name)
		{
		}

		BlueChanger::~BlueChanger()
		{
		}

		Animator* BlueChanger::createInstance(chstr name)
		{
			return new BlueChanger(name);
		}

		float BlueChanger::_getObjectValue()
		{
			return (float)this->parent->getBlue();
		}

		void BlueChanger::_setObjectValue(float value)
		{
			this->parent->setBlue((unsigned char)value);
		}

		void BlueChanger::update(float timeDelta)
		{
			this->_valueUpdateUChar(timeDelta);
		}
		
	}
}
