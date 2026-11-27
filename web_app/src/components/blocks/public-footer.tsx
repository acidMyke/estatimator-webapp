import { Link } from '@tanstack/react-router';

import { PUBLIC_NAVIGATIONS } from '@/lib/constants';

import { Logo } from './logo';
export function PublicFooter() {
  return (
    <footer className='border-t'>
      <div className='mx-auto flex w-full max-w-6xl flex-col gap-8 px-4 py-10'>
        <div className='flex flex-col gap-8 sm:flex-row sm:items-start sm:justify-between'>
          <div className='flex flex-col gap-3'>
            <Logo />
            <p className='max-w-sm text-sm text-muted-foreground'>
              Singapore HDB prices, made predictable. Data-driven resale valuation for every flat.
            </p>
          </div>
          <nav className='flex flex-col gap-2 text-sm' aria-label='Footer navigation'>
            <span className='font-medium text-foreground'>Product</span>
            {PUBLIC_NAVIGATIONS.map(
              ({ label, showFooter, to }) =>
                showFooter && (
                  <Link to={to} key={to} className='text-muted-foreground transition-colors hover:text-foreground'>
                    {label}
                  </Link>
                ),
            )}
          </nav>
        </div>
      </div>
    </footer>
  );
}
