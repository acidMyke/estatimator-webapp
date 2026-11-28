import { createFileRoute, Outlet } from '@tanstack/react-router';

export const Route = createFileRoute('/admin')({
  component: LayoutComponent,
});

function LayoutComponent() {
  return (
    <div>
      <Outlet />
    </div>
  );
}
