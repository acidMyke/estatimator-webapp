import { createFileRoute, Outlet } from '@tanstack/react-router';

import { PublicFooter } from '@/components/blocks/public-footer';
import { PublicHeader } from '@/components/blocks/public-header';

export const Route = createFileRoute('/_public')({
  component: RouteComponent,
});

function RouteComponent() {
  return (
    <div className='flex min-h-screen flex-col'>
      <PublicHeader />
      <div className='flex-1'>
        <Outlet />
      </div>
      <PublicFooter />
    </div>
  );
}
