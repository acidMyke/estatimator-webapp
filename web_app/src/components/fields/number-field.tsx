import { useId } from 'react';
import type { ComponentProps, ReactNode } from 'react';

import { Field, FieldDescription, FieldError, FieldLabel } from '@/components/ui/field';
import { Input } from '@/components/ui/input';
import { useFieldContext } from '@/hooks/form-context';

import { useFieldErrorState } from './field-errors';

export type NumberFieldProps = Omit<ComponentProps<typeof Input>, 'id' | 'value' | 'onChange' | 'onBlur' | 'type'> & {
  label: ReactNode;
  description?: ReactNode;
};

export function NumberField({ label, description, ...inputProps }: NumberFieldProps) {
  const field = useFieldContext<number | null>();
  const id = useId();
  const { isInvalid, errors } = useFieldErrorState(field);

  return (
    <Field data-invalid={isInvalid || undefined}>
      <FieldLabel htmlFor={id}>{label}</FieldLabel>
      <Input
        {...inputProps}
        id={id}
        type='number'
        inputMode='decimal'
        value={field.state.value ?? ''}
        onChange={event => {
          const next = event.target.value === '' ? Number.NaN : Number(event.target.value);
          field.handleChange(Number.isNaN(next) ? null : next);
        }}
        onBlur={field.handleBlur}
        aria-invalid={isInvalid || undefined}
      />
      {description && <FieldDescription>{description}</FieldDescription>}
      {isInvalid && <FieldError errors={errors} />}
    </Field>
  );
}
