/// @file
/// @version 2.2
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://opensource.org/licenses/BSD-3-Clause

#include "AffectorResizer.h"
#include "aprilparticleUtil.h"
#include "Particle.h"

namespace aprilparticle
{
	namespace Affectors
	{
		harray<PropertyDescription> Resizer::_propertyDescriptions;

		Resizer::Resizer(chstr name) : Affector(name)
		{
			this->startSize.set(1.0f, 1.0f);
			this->endSize.set(0.0f, 0.0f);
		}

		Resizer::Resizer(gvec2 startSize, gvec2 endSize, chstr name) : Affector(name)
		{
			this->startSize = startSize;
			this->endSize = endSize;
		}

		Resizer::~Resizer()
		{
		}
		
		Affector* Resizer::createInstance(chstr name)
		{
			return new Resizer(name);
		}

		harray<PropertyDescription> Resizer::getPropertyDescriptions()
		{
			if (Resizer::_propertyDescriptions.size() == 0)
			{
				Resizer::_propertyDescriptions += PropertyDescription("start_size", PropertyDescription::GVEC2);
				Resizer::_propertyDescriptions += PropertyDescription("end_size", PropertyDescription::GVEC2);
			}
			return (Affector::getPropertyDescriptions() + Resizer::_propertyDescriptions);
		}

		hstr Resizer::getProperty(chstr name)
		{
			if (name == "start_size")	return gvec2_to_hstr(this->getStartSize());
			if (name == "end_size")		return gvec2_to_hstr(this->getEndSize());
			return Affector::getProperty(name);
		}

		bool Resizer::setProperty(chstr name, chstr value)
		{
			if		(name == "start_size")	this->setStartSize(hstr_to_gvec2(value));
			else if	(name == "end_size")	this->setEndSize(hstr_to_gvec2(value));
			else return Affector::setProperty(name, value);
			return true;
		}

		void Resizer::update(Particle* particle, float timeDelta, gvec3& movement)
		{
			this->_ratio = particle->getLifeProgressRatio();
			particle->size = this->startSize * (1.0f - this->_ratio) + this->endSize * this->_ratio;
		}

	}

}

