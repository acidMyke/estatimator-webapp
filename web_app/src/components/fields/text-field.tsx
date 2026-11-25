import { useId } from 'react';
import type { ComponentProps, ReactNode } from 'react';

import { Field, FieldDescription, FieldError, FieldLabel } from '@/components/ui/field';
import { Input } from '@/components/ui/input';
import { useFieldContext } from '@/hooks/form-context';

import { useFieldErrorState } from './field-errors';

export type TextFieldProps = Omit<ComponentProps<typeof Input>, 'id' | 'value' | 'onChange' | 'onBlur'> & {
  label: ReactNode;
  description?: ReactNode;
};

export function TextField({ label, description, ...inputProps }: TextFieldProps) {
  const field = useFieldContext<string>();
  const id = useId();
  const { isInvalid, errors } = useFieldErrorState(field);

  return (
    <Field data-invalid={isInvalid || undefined}>
      <FieldLabel htmlFor={id}>{label}</FieldLabel>
      <Input
        {...inputProps}
        id={id}
        value={field.state.value ?? ''}
        onChange={event => field.handleChange(event.target.value)}
        onBlur={field.handleBlur}
        aria-invalid={isInvalid || undefined}
      />
      {description && <FieldDescription>{description}</FieldDescription>}
      {isInvalid && <FieldError errors={errors} />}
    </Field>
  );
}
