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
/// Defines an animator that can scale objects horizontally.

#ifndef APRILUI_SCALER_X_H
#define APRILUI_SCALER_X_H

#include <hltypes/hstring.h>

#include "Animator.h"

namespace aprilui
{
	namespace Animators
	{
		class apriluiExport ScalerX : public Animator
		{
		public:
			ScalerX(chstr name);
			~ScalerX();
			hstr getClassName() const { return "ScalerX"; }

			static Animator* createInstance(chstr name);
			
			void update(float timeDelta);
			
		protected:
			float _getObjectValue();
			void _setObjectValue(float value);
			
		};
	}
}

#endif
