import { useSelector } from '@tanstack/react-form';
import type { AnyFieldApi } from '@tanstack/react-form';
import { useMemo } from 'react';

export type FieldErrorMessages = Array<{ message?: string }>;

export function toErrorMessages(errors: readonly unknown[]): FieldErrorMessages {
  return errors.flatMap(error => {
    if (typeof error === 'string') {
      return [{ message: error }];
    }

    if (error && typeof error === 'object' && 'message' in error && typeof error.message === 'string') {
      return [{ message: error.message }];
    }

    return [];
  });
}

export function useFieldErrorState(field: AnyFieldApi) {
  const errors = useSelector(field.store, state => state.meta.errors);
  const isTouched = useSelector(field.store, state => state.meta.isTouched);

  return useMemo(
    () => ({
      isInvalid: isTouched && errors.length > 0,
      errors: toErrorMessages(errors),
    }),
    [errors, isTouched],
  );
}
