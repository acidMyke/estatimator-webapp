import { Link } from '@tanstack/react-router';

import { PUBLIC_NAVIGATIONS } from '@/lib/constants';

import { Logo } from './logo';

export function PublicHeader() {
  return (
    <header className='sticky top-0 z-40 w-full border-b bg-background/80 backdrop-blur-sm'>
      <div className='mx-auto flex h-16 w-full max-w-6xl items-center justify-between gap-4 px-4 sm:px-6'>
        <Link to='/' className='shrink-0' aria-label='HDBeePrice home'>
          <Logo />
        </Link>

        <nav className='flex items-center gap-6' aria-label='Main navigation'>
          {PUBLIC_NAVIGATIONS.map(
            ({ label, showHeader, to }) =>
              showHeader && (
                <Link
                  to={to}
                  key={to}
                  className='text-sm font-medium text-muted-foreground transition-colors hover:text-foreground'
                  activeProps={{ className: 'text-foreground' }}
                >
                  {label}
                </Link>
              ),
          )}
        </nav>
      </div>
    </header>
  );
}
