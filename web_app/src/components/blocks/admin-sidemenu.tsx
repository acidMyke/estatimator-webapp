import { Link } from '@tanstack/react-router';

import { ADMIN_NAVIGATIONS } from '@/lib/constants';

import { Logo } from './logo';

export function AdminSidemenu() {
  return (
    <aside className='sticky top-14 flex h-[calc(100dvh-3.5rem)] w-64 shrink-0 flex-col gap-5 overflow-y-auto border-r border-sidebar-border bg-sidebar/90 p-4 backdrop-blur-sm'>
      <div className='flex flex-col gap-2 border-b px-2 pb-2'>
        <Logo />
        <span className='text-sm tracking-wider text-sidebar-foreground/80 uppercase'>Admin Dashboard</span>
      </div>

      <nav className='flex flex-col gap-1' aria-label='Admin navigation'>
        {ADMIN_NAVIGATIONS.map(({ to, label, icon: Icon }) => (
          <Link
            to={to}
            key={to}
            className='flex h-10 w-full items-center gap-3 rounded-md px-3 text-sm text-sidebar-foreground/80 [:hover,[data-active="true"]]:bg-sidebar-accent [:hover,[data-active="true"]]:text-sidebar-accent-foreground'
            activeOptions={{ exact: true }}
            activeProps={{ 'data-active': true }}
          >
            <Icon />
            {label}
          </Link>
        ))}
      </nav>
    </aside>
  );
}
