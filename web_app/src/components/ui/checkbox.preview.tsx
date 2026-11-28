import { Checkbox } from '@/components/ui/checkbox';
import { Field, FieldDescription, FieldError, FieldGroup, FieldLabel } from '@/components/ui/field';

export const States = () => (
  <div className='flex flex-wrap items-center gap-6'>
    <div className='flex items-center gap-2'>
      <Checkbox id='checkbox-unchecked' />
      <FieldLabel htmlFor='checkbox-unchecked' className='font-normal'>
        Unchecked
      </FieldLabel>
    </div>
    <div className='flex items-center gap-2'>
      <Checkbox id='checkbox-checked' defaultChecked />
      <FieldLabel htmlFor='checkbox-checked' className='font-normal'>
        Checked
      </FieldLabel>
    </div>
    <div className='flex items-center gap-2'>
      <Checkbox id='checkbox-indeterminate' indeterminate />
      <FieldLabel htmlFor='checkbox-indeterminate' className='font-normal'>
        Indeterminate
      </FieldLabel>
    </div>
    <div className='flex items-center gap-2'>
      <Checkbox id='checkbox-disabled' disabled />
      <FieldLabel htmlFor='checkbox-disabled' className='font-normal'>
        Disabled
      </FieldLabel>
    </div>
    <div className='flex items-center gap-2'>
      <Checkbox id='checkbox-disabled-checked' defaultChecked disabled />
      <FieldLabel htmlFor='checkbox-disabled-checked' className='font-normal'>
        Disabled checked
      </FieldLabel>
    </div>
  </div>
);

export const WithLabels = () => (
  <FieldGroup className='max-w-md'>
    <Field orientation='horizontal'>
      <Checkbox id='checkbox-newsletter' defaultChecked />
      <FieldLabel htmlFor='checkbox-newsletter' className='font-normal'>
        Product updates
      </FieldLabel>
    </Field>
    <Field orientation='horizontal'>
      <Checkbox id='checkbox-marketing' />
      <FieldLabel htmlFor='checkbox-marketing' className='font-normal'>
        Marketing emails
      </FieldLabel>
    </Field>
  </FieldGroup>
);

export const Invalid = () => (
  <Field data-invalid className='max-w-md'>
    <div className='flex items-center gap-2'>
      <Checkbox id='checkbox-terms' aria-invalid />
      <FieldLabel htmlFor='checkbox-terms'>Accept terms and conditions</FieldLabel>
    </div>
    <FieldDescription>You must accept the terms before continuing.</FieldDescription>
    <FieldError>This field is required.</FieldError>
  </Field>
);
