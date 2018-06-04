console.log('start');

import {
	val,
	inc
} from './mod1';

import * as m2 from './mod2';

import * as mod from './mod1';

console.log(val);

inc();
console.log(val);

console.log(mod.val);
mod.inc()
console.log(val);