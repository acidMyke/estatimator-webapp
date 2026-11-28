import { createFileRoute, Outlet } from '@tanstack/react-router';

export const Route = createFileRoute('/admin/_dash')({
  component: LayoutComponent,
});

function LayoutComponent() {
  return (
    <div>
      <Outlet />
    </div>
  );
}
