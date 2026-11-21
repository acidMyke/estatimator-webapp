import { useId } from 'react';
import type { ComponentProps, ReactNode } from 'react';

import { Field, FieldContent, FieldDescription, FieldError, FieldLabel } from '#components/ui/field';
import { Switch } from '#components/ui/switch';
import { useFieldContext } from '#hooks/form-context';

import { useFieldErrorState } from './field-errors';

export type SwitchFieldProps = Omit<
  ComponentProps<typeof Switch>,
  'children' | 'id' | 'checked' | 'defaultChecked' | 'onCheckedChange'
> & {
  label: ReactNode;
  description?: ReactNode;
};

export function SwitchField({ label, description, ...switchProps }: SwitchFieldProps) {
  const field = useFieldContext<boolean>();
  const id = useId();
  const { isInvalid, errors } = useFieldErrorState(field);

  return (
    <Field orientation='horizontal' data-invalid={isInvalid || undefined}>
      <FieldContent>
        <FieldLabel htmlFor={id}>{label}</FieldLabel>
        {description && <FieldDescription>{description}</FieldDescription>}
        {isInvalid && <FieldError errors={errors} />}
      </FieldContent>
      <Switch
        {...switchProps}
        id={id}
        checked={field.state.value ?? false}
        onCheckedChange={checked => field.handleChange(checked)}
        onBlur={field.handleBlur}
        aria-invalid={isInvalid || undefined}
      />
    </Field>
  );
}
