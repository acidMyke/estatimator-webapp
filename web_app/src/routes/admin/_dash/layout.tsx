import { createFileRoute, Outlet } from '@tanstack/react-router';

import { AdminSidemenu } from '@/components/blocks/admin-sidemenu';

export const Route = createFileRoute('/admin/_dash')({
  component: LayoutComponent,
});

function LayoutComponent() {
  return (
    <div className='flex flex-1'>
      <AdminSidemenu />
      <main className='min-w-0 flex-1 p-6 sm:p-8'>
        <Outlet />
      </main>
    </div>
  );
}
