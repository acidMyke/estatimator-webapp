import { IconDatabase, IconFlask, IconGitCompare, IconHome } from '@tabler/icons-react';
import { linkOptions } from '@tanstack/react-router';

export const PUBLIC_NAVIGATIONS = linkOptions([
  {
    to: '/about',
    label: 'About',
    showHeader: true,
    showFooter: true,
  },
  {
    to: '/login',
    label: 'Login',
    showHeader: true,
    showFooter: false,
  },
  {
    to: '/register',
    label: 'Register',
    showHeader: true,
    showFooter: false,
  },
]);

export const ADMIN_NAVIGATIONS = linkOptions([
  {
    to: '/admin',
    label: 'Dashboard',
    icon: IconHome,
  },
  {
    to: '/admin/data-management',
    label: 'Data Management',
    icon: IconDatabase,
  },
  {
    to: '/admin/training-studio',
    label: 'Training Studio',
    icon: IconFlask,
  },
  {
    to: '/admin/compare-and-deploy',
    label: 'Compare & Deploy',
    icon: IconGitCompare,
  },
]);
