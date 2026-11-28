import { useId } from 'react';
import type { ComponentProps, ReactNode } from 'react';

import { Field, FieldDescription, FieldError, FieldLabel } from '@/components/ui/field';
import { Textarea } from '@/components/ui/textarea';
import { useFieldContext } from '@/hooks/form-context';

import { useFieldErrorState } from './field-errors';

export type TextareaFieldProps = Omit<ComponentProps<typeof Textarea>, 'id' | 'value' | 'onChange' | 'onBlur'> & {
  label: ReactNode;
  description?: ReactNode;
};

export function TextareaField({ label, description, ...textareaProps }: TextareaFieldProps) {
  const field = useFieldContext<string>();
  const id = useId();
  const { isInvalid, errors } = useFieldErrorState(field);

  return (
    <Field data-invalid={isInvalid || undefined}>
      <FieldLabel htmlFor={id}>{label}</FieldLabel>
      <Textarea
        {...textareaProps}
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
