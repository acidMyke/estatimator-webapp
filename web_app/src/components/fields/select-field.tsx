import { useId } from 'react';
import type { ComponentProps, ReactNode } from 'react';

import { Field, FieldDescription, FieldError, FieldLabel } from '#components/ui/field';
import { Select, SelectContent, SelectGroup, SelectItem, SelectTrigger, SelectValue } from '#components/ui/select';
import { useFieldContext } from '#hooks/form-context';

import { useFieldErrorState } from './field-errors';

export type SelectOption<TValue extends string = string> = {
  label: ReactNode;
  value: TValue;
};

export type SelectFieldProps<TValue extends string> = Omit<
  ComponentProps<typeof Select>,
  'children' | 'items' | 'multiple' | 'value' | 'defaultValue' | 'onValueChange'
> & {
  label: ReactNode;
  description?: ReactNode;
  placeholder?: string;
  options: ReadonlyArray<SelectOption<TValue>>;
};

export function SelectField<TValue extends string>({
  label,
  description,
  placeholder,
  options,
  ...selectProps
}: SelectFieldProps<TValue>) {
  const field = useFieldContext<TValue>();
  const id = useId();
  const { isInvalid, errors } = useFieldErrorState(field);

  return (
    <Field data-invalid={isInvalid || undefined}>
      <FieldLabel htmlFor={id}>{label}</FieldLabel>
      <Select
        {...selectProps}
        items={options}
        value={field.state.value ?? null}
        onValueChange={value => {
          if (value !== null) {
            field.handleChange(value as TValue);
          }
        }}
      >
        <SelectTrigger id={id} className='w-full' onBlur={field.handleBlur} aria-invalid={isInvalid || undefined}>
          <SelectValue placeholder={placeholder} />
        </SelectTrigger>
        <SelectContent>
          <SelectGroup>
            {options.map(option => (
              <SelectItem key={option.value} value={option.value}>
                {option.label}
              </SelectItem>
            ))}
          </SelectGroup>
        </SelectContent>
      </Select>
      {description && <FieldDescription>{description}</FieldDescription>}
      {isInvalid && <FieldError errors={errors} />}
    </Field>
  );
}
