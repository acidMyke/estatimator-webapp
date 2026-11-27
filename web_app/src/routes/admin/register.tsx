import { createFileRoute } from '@tanstack/react-router';

import { PlaceholderPage } from '@/components/blocks/placeholder-page';

export const Route = createFileRoute('/admin/register')({
  component: RouteComponent,
});

function RouteComponent() {
  return <PlaceholderPage title='Admin register'></PlaceholderPage>;
}
