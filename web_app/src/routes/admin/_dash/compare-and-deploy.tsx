import { createFileRoute } from '@tanstack/react-router';

import { PlaceholderPage } from '@/components/blocks/placeholder-page';

export const Route = createFileRoute('/admin/_dash/compare-and-deploy')({
  component: RouteComponent,
});

function RouteComponent() {
  return <PlaceholderPage title='Compare & Deploy' />;
}
