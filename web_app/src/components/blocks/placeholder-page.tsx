import type { ReactNode } from 'react';

type PlaceholderPageProps = {
  title: string;
  children?: ReactNode;
};

export function PlaceholderPage({ title, children }: PlaceholderPageProps) {
  return (
    <div className='mx-auto flex w-full max-w-2xl flex-col items-center gap-2 border px-4 py-8 text-center'>
      <h1 className='font-heading text-3xl font-semibold'>Stay tuned!!</h1>
      <p className='font-heading text-xl'>We're cooking something for you</p>
      <p className='mt-4 text-sm italic'>{title}</p>
      {children}
    </div>
  );
}
