import { useId } from 'react';
import type { ComponentProps, ReactNode } from 'react';

import { Checkbox } from '@/components/ui/checkbox';
import { Field, FieldContent, FieldDescription, FieldError, FieldLabel } from '@/components/ui/field';
import { useFieldContext } from '@/hooks/form-context';

import { useFieldErrorState } from './field-errors';

export type CheckboxFieldProps = Omit<
  ComponentProps<typeof Checkbox>,
  'children' | 'id' | 'checked' | 'defaultChecked' | 'onCheckedChange'
> & {
  label: ReactNode;
  description?: ReactNode;
};

export function CheckboxField({ label, description, ...checkboxProps }: CheckboxFieldProps) {
  const field = useFieldContext<boolean>();
  const id = useId();
  const { isInvalid, errors } = useFieldErrorState(field);

  return (
    <Field orientation='horizontal' data-invalid={isInvalid || undefined}>
      <Checkbox
        {...checkboxProps}
        id={id}
        checked={field.state.value ?? false}
        onCheckedChange={checked => field.handleChange(checked)}
        onBlur={field.handleBlur}
        aria-invalid={isInvalid || undefined}
      />
      <FieldContent>
        <FieldLabel htmlFor={id}>{label}</FieldLabel>
        {description && <FieldDescription>{description}</FieldDescription>}
        {isInvalid && <FieldError errors={errors} />}
      </FieldContent>
    </Field>
  );
}
