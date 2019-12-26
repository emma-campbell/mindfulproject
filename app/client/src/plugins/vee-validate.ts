import {
  required,
  confirmed,
  email,
  min,
} from 'vee-validate/dist/rules';

import { extend } from 'vee-validate';

extend('required', {
  ...required,
  message: 'This field is required',
});

extend('email', {
  ...email,
  message: 'This field must be a valid email',
});

extend('confirmed', {
  ...confirmed,
  message: 'The password confirmation does not match',
});

extend('min', {
  ...min,
  message: 'This field does not meet the minimum length requirement',
});
