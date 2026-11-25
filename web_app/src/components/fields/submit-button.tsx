import type { ComponentProps, ReactNode } from 'react';

import { Button } from '@/components/ui/button';
import { useFormContext } from '@/hooks/form-context';

export type SubmitButtonProps = ComponentProps<typeof Button> & {
  pendingLabel?: ReactNode;
};

export function SubmitButton({ children, pendingLabel = 'Submitting...', ...buttonProps }: SubmitButtonProps) {
  const form = useFormContext();

  return (
    <form.Subscribe selector={state => state.isSubmitting}>
      {isSubmitting => (
        <Button
          {...buttonProps}
          type='submit'
          disabled={isSubmitting || buttonProps.disabled}
          aria-busy={isSubmitting || undefined}
        >
          {isSubmitting ? pendingLabel : children}
        </Button>
      )}
    </form.Subscribe>
  );
}
