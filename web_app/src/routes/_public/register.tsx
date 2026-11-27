import { createFileRoute } from '@tanstack/react-router';

import { PlaceholderPage } from '@/components/blocks/placeholder-page';

export const Route = createFileRoute('/_public/register')({
  component: RouteComponent,
});

function RouteComponent() {
  return <PlaceholderPage title='Public register'></PlaceholderPage>;
}
