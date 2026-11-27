import type { ReactNode } from 'react';

type PlaceholderPageProps = {
  title: string;
  children?: ReactNode;
};

export function PlaceholderPage({ title, children }: PlaceholderPageProps) {
  return (
    <div className='mx-auto flex w-full max-w-2xl flex-col items-center gap-6 border px-4 py-16 text-center sm:py-24'>
      <h1 className='font-heading text-3xl font-semibold'>Placeholder Page: {title}</h1>
      {children}
    </div>
  );
}
