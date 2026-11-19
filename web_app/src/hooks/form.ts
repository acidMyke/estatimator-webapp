import { createFormHook } from '@tanstack/react-form';

import { CheckboxField } from '#form/checkbox-field';
import { NumberField } from '#form/number-field';
import { SelectField } from '#form/select-field';
import { SubmitButton } from '#form/submit-button';
import { SwitchField } from '#form/switch-field';
import { TextField } from '#form/text-field';
import { TextareaField } from '#form/textarea-field';

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
