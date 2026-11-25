import { createFormHook } from '@tanstack/react-form';

import { CheckboxField } from '@/components/fields/checkbox-field';
import { NumberField } from '@/components/fields/number-field';
import { SelectField } from '@/components/fields/select-field';
import { SubmitButton } from '@/components/fields/submit-button';
import { SwitchField } from '@/components/fields/switch-field';
import { TextField } from '@/components/fields/text-field';
import { TextareaField } from '@/components/fields/textarea-field';

import { fieldContext, formContext } from './form-context';

export const { useAppForm, withForm, withFieldGroup, useTypedAppFormContext, extendForm } = createFormHook({
  fieldContext,
  formContext,
  fieldComponents: {
    TextField,
    TextareaField,
    NumberField,
    SelectField,
    CheckboxField,
    SwitchField,
  },
  formComponents: {
    SubmitButton,
  },
});

export { fieldContext, formContext, useFieldContext, useFormContext } from './form-context';
