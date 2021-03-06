/// @file
/// @version 2.2
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://opensource.org/licenses/BSD-3-Clause

#include <hltypes/harray.h>
#include <hltypes/hstring.h>

#include "AffectorAttractor.h"
#include "aprilparticleUtil.h"
#include "Particle.h"
#include "Space.h"

namespace aprilparticle
{
	namespace Affectors
	{
		harray<PropertyDescription> Attractor::_propertyDescriptions;

		Attractor::Attractor(chstr name) : Space(name)
		{
			this->force = 1.0f;
			this->exponent = 2.0f;
		}
		
		Attractor::Attractor(gvec3 position, float radius, float force, float exponent, chstr name) : Space(position, radius, name)
		{
			this->force = force;
			this->exponent = exponent;
		}

		Attractor::~Attractor()
		{
		}
		
		Affector* Attractor::createInstance(chstr name)
		{
			return new Attractor(name);
		}

		harray<PropertyDescription> Attractor::getPropertyDescriptions()
		{
			if (Attractor::_propertyDescriptions.size() == 0)
			{
				Attractor::_propertyDescriptions += PropertyDescription("force", PropertyDescription::FLOAT);
				Attractor::_propertyDescriptions += PropertyDescription("exponent", PropertyDescription::FLOAT);
			}
			return (Space::getPropertyDescriptions() + Attractor::_propertyDescriptions);
		}

		hstr Attractor::getProperty(chstr name)
		{
			if (name == "force")	return this->getForce();
			if (name == "exponent")	return this->getExponent();
			return Space::getProperty(name);
		}

		bool Attractor::setProperty(chstr name, chstr value)
		{
			if		(name == "force")		this->setForce(value);
			else if	(name == "exponent")	this->setExponent(value);
			else return Space::setProperty(name, value);
			return true;
		}

		void Attractor::update(Particle* particle, float timeDelta, gvec3& movement)
		{
			this->_direction = this->position + this->space->getPosition() - particle->position;
			this->_squaredLength = this->_direction.squaredLength();
			if (is_inside(this->_squaredLength, 0.02f, this->radius * this->radius))
			{
				this->_factor = (this->radius - hsqrt(this->_squaredLength)) / this->radius;
				if (this->exponent != 1.0f)
				{
					if (this->exponent == (int)this->exponent)
					{
						this->_factor = pow(this->_factor, (int)this->exponent);
					}
					else
					{
						this->_factor = pow(this->_factor, this->exponent);
					}
				}
				movement += this->_direction.normalized() * (RAND_RANGE(Randomness) * this->force * this->_factor * timeDelta);
			}
		}

	}

}

