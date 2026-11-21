"""Contains all the data models used in inputs/outputs"""

from .acme_challenge import AcmeChallenge
from .app import App
from .app_organization_info import AppOrganizationInfo
from .app_secret import AppSecret
from .app_secrets import AppSecrets
from .app_secrets_update_request import AppSecretsUpdateRequest
from .app_secrets_update_request_values import AppSecretsUpdateRequestValues
from .app_secrets_update_resp import AppSecretsUpdateResp
from .app_status import AppStatus
from .assign_ip_request import AssignIPRequest
from .assign_ip_response import AssignIPResponse
from .authenticate_token_request import AuthenticateTokenRequest
from .authorize_response import AuthorizeResponse
from .authorize_token_request import AuthorizeTokenRequest
from .certificate_check_response import CertificateCheckResponse
from .certificate_detail import CertificateDetail
from .certificate_entry import CertificateEntry
from .certificate_entry_source import CertificateEntrySource
from .certificate_entry_status import CertificateEntryStatus
from .certificate_summary import CertificateSummary
from .certificate_validation import CertificateValidation
from .certificate_validation_error import CertificateValidationError
from .check_status import CheckStatus
from .check_status_status import CheckStatusStatus
from .create_acme_certificate_request import CreateAcmeCertificateRequest
from .create_app_deploy_token_request import CreateAppDeployTokenRequest
from .create_app_deploy_token_response import CreateAppDeployTokenResponse
from .create_app_request import CreateAppRequest
from .create_app_response import CreateAppResponse
from .create_custom_certificate_request import CreateCustomCertificateRequest
from .create_lease_request import CreateLeaseRequest
from .create_machine_request import CreateMachineRequest
from .create_oidc_token_request import CreateOIDCTokenRequest
from .create_postgres_attachment_request import CreatePostgresAttachmentRequest
from .create_postgres_attachment_response import CreatePostgresAttachmentResponse
from .create_postgres_backup_request import CreatePostgresBackupRequest
from .create_postgres_backup_request_type import CreatePostgresBackupRequestType
from .create_postgres_cluster_request import CreatePostgresClusterRequest
from .create_postgres_cluster_request_pg_major_version import (
    CreatePostgresClusterRequestPgMajorVersion,
)
from .create_postgres_cluster_request_plan import CreatePostgresClusterRequestPlan
from .create_postgres_cluster_request_pool_mode import (
    CreatePostgresClusterRequestPoolMode,
)
from .create_postgres_database_request import CreatePostgresDatabaseRequest
from .create_postgres_user_request import CreatePostgresUserRequest
from .create_postgres_user_request_role import CreatePostgresUserRequestRole
from .create_postgres_user_response import CreatePostgresUserResponse
from .create_volume_request import CreateVolumeRequest
from .create_volume_request_fstype import CreateVolumeRequestFstype
from .current_token_response import CurrentTokenResponse
from .decrypt_secretkey_request import DecryptSecretkeyRequest
from .decrypt_secretkey_response import DecryptSecretkeyResponse
from .delete_app_secret_response import DeleteAppSecretResponse
from .delete_secretkey_response import DeleteSecretkeyResponse
from .destroy_custom_certificate_response import DestroyCustomCertificateResponse
from .dns_records import DNSRecords
from .dns_requirements import DNSRequirements
from .enable_postgres_extension_request import EnablePostgresExtensionRequest
from .encrypt_secretkey_request import EncryptSecretkeyRequest
from .encrypt_secretkey_response import EncryptSecretkeyResponse
from .error_response import ErrorResponse
from .error_response_details import ErrorResponseDetails
from .exec_response import ExecResponse
from .extend_volume_request import ExtendVolumeRequest
from .extend_volume_response import ExtendVolumeResponse
from .fly_container_config import FlyContainerConfig
from .fly_container_config_env import FlyContainerConfigEnv
from .fly_container_dependency import FlyContainerDependency
from .fly_container_dependency_condition import FlyContainerDependencyCondition
from .fly_container_healthcheck import FlyContainerHealthcheck
from .fly_container_healthcheck_kind import FlyContainerHealthcheckKind
from .fly_container_healthcheck_scheme import FlyContainerHealthcheckScheme
from .fly_dns_config import FlyDNSConfig
from .fly_dns_forward_rule import FlyDnsForwardRule
from .fly_dns_option import FlyDnsOption
from .fly_env_from import FlyEnvFrom
from .fly_env_from_field_ref import FlyEnvFromFieldRef
from .fly_exec_healthcheck import FlyExecHealthcheck
from .fly_file import FlyFile
from .fly_http_healthcheck import FlyHTTPHealthcheck
from .fly_http_options import FlyHTTPOptions
from .fly_http_response_options import FlyHTTPResponseOptions
from .fly_http_response_options_headers import FlyHTTPResponseOptionsHeaders
from .fly_http_response_options_headers_additional_property import (
    FlyHTTPResponseOptionsHeadersAdditionalProperty,
)
from .fly_machine_cache_drive import FlyMachineCacheDrive
from .fly_machine_check import FlyMachineCheck
from .fly_machine_check_kind import FlyMachineCheckKind
from .fly_machine_config import FlyMachineConfig
from .fly_machine_config_checks import FlyMachineConfigChecks
from .fly_machine_config_env import FlyMachineConfigEnv
from .fly_machine_config_metadata import FlyMachineConfigMetadata
from .fly_machine_guest import FlyMachineGuest
from .fly_machine_guest_persist_rootfs import FlyMachineGuestPersistRootfs
from .fly_machine_http_header import FlyMachineHTTPHeader
from .fly_machine_init import FlyMachineInit
from .fly_machine_metrics import FlyMachineMetrics
from .fly_machine_mount import FlyMachineMount
from .fly_machine_port import FlyMachinePort
from .fly_machine_process import FlyMachineProcess
from .fly_machine_process_env import FlyMachineProcessEnv
from .fly_machine_restart import FlyMachineRestart
from .fly_machine_restart_policy import FlyMachineRestartPolicy
from .fly_machine_rootfs import FlyMachineRootfs
from .fly_machine_rootfs_persist import FlyMachineRootfsPersist
from .fly_machine_secret import FlyMachineSecret
from .fly_machine_service import FlyMachineService
from .fly_machine_service_autostop import FlyMachineServiceAutostop
from .fly_machine_service_check import FlyMachineServiceCheck
from .fly_machine_service_concurrency import FlyMachineServiceConcurrency
from .fly_machine_spot import FlyMachineSpot
from .fly_proxy_proto_options import FlyProxyProtoOptions
from .fly_replay_cache import FlyReplayCache
from .fly_replay_cache_type import FlyReplayCacheType
from .fly_static import FlyStatic
from .fly_stop_config import FlyStopConfig
from .fly_stop_config_signal import FlyStopConfigSignal
from .fly_tcp_healthcheck import FlyTCPHealthcheck
from .fly_tls_options import FlyTLSOptions
from .fly_unhealthy_policy import FlyUnhealthyPolicy
from .flyio_access import FlyioAccess
from .fork_postgres_cluster_request import ForkPostgresClusterRequest
from .fork_postgres_cluster_request_plan import ForkPostgresClusterRequestPlan
from .get_postgres_user_credentials_response import GetPostgresUserCredentialsResponse
from .image_ref import ImageRef
from .image_ref_labels import ImageRefLabels
from .ip_assignment import IPAssignment
from .ip_assignment_network import IPAssignmentNetwork
from .ip_assignment_type import IPAssignmentType
from .ip_pair import IPPair
from .issued_certificate import IssuedCertificate
from .issued_certificate_type import IssuedCertificateType
from .lease import Lease
from .lease_error_response import LeaseErrorResponse
from .lease_error_response_status import LeaseErrorResponseStatus
from .lease_ok_response import LeaseOkResponse
from .lease_ok_response_status import LeaseOkResponseStatus
from .lease_response import LeaseResponse
from .lease_response_status import LeaseResponseStatus
from .list_apps_response import ListAppsResponse
from .list_certificates_response import ListCertificatesResponse
from .list_ip_assignments_response import ListIPAssignmentsResponse
from .list_postgres_active_queries_response import ListPostgresActiveQueriesResponse
from .list_postgres_backups_response import ListPostgresBackupsResponse
from .list_postgres_clusters_response import ListPostgresClustersResponse
from .list_postgres_databases_response import ListPostgresDatabasesResponse
from .list_postgres_extensions_response import ListPostgresExtensionsResponse
from .list_postgres_plans_response import ListPostgresPlansResponse
from .list_postgres_slow_queries_response import ListPostgresSlowQueriesResponse
from .list_postgres_users_response import ListPostgresUsersResponse
from .listen_socket import ListenSocket
from .macaroon_caveat_set import MacaroonCaveatSet
from .macaroon_caveat_set_caveats_item import MacaroonCaveatSetCaveatsItem
from .macaroon_nonce import MacaroonNonce
from .machine import Machine
from .machine_event import MachineEvent
from .machine_event_request import MachineEventRequest
from .machine_exec_request import MachineExecRequest
from .machine_host_status import MachineHostStatus
from .machine_overview_config import MachineOverviewConfig
from .machine_overview_config_metadata import MachineOverviewConfigMetadata
from .machine_version import MachineVersion
from .machines_list_processes_order import MachinesListProcessesOrder
from .machines_list_processes_sort_by import MachinesListProcessesSortBy
from .machines_restart_signal import MachinesRestartSignal
from .machines_show_metadata_response_200 import MachinesShowMetadataResponse200
from .machines_wait_state import MachinesWaitState
from .main_get_placements_request import MainGetPlacementsRequest
from .main_get_placements_response import MainGetPlacementsResponse
from .main_memory_response import MainMemoryResponse
from .main_reclaim_memory_request import MainReclaimMemoryRequest
from .main_reclaim_memory_response import MainReclaimMemoryResponse
from .main_region_response import MainRegionResponse
from .main_region_row import MainRegionRow
from .main_region_row_geo_region import MainRegionRowGeoRegion
from .main_set_memory_limit_request import MainSetMemoryLimitRequest
from .main_status_code import MainStatusCode
from .main_token_access import MainTokenAccess
from .main_token_info import MainTokenInfo
from .metadata_value_response import MetadataValueResponse
from .ok_response import OkResponse
from .org_machine import OrgMachine
from .org_machines_response import OrgMachinesResponse
from .org_volume import OrgVolume
from .org_volume_host_status import OrgVolumeHostStatus
from .org_volume_type import OrgVolumeType
from .org_volumes_response import OrgVolumesResponse
from .organization_ref import OrganizationRef
from .ownership_verification import OwnershipVerification
from .placement_region_placement import PlacementRegionPlacement
from .placement_weights import PlacementWeights
from .postgres_active_query import PostgresActiveQuery
from .postgres_attached_app import PostgresAttachedApp
from .postgres_attachment import PostgresAttachment
from .postgres_backup import PostgresBackup
from .postgres_backup_type import PostgresBackupType
from .postgres_cluster import PostgresCluster
from .postgres_cluster_cpu_kind import PostgresClusterCpuKind
from .postgres_cluster_endpoints import PostgresClusterEndpoints
from .postgres_cluster_pg_major_version import PostgresClusterPgMajorVersion
from .postgres_cluster_plan import PostgresClusterPlan
from .postgres_cluster_status import PostgresClusterStatus
from .postgres_cluster_summary import PostgresClusterSummary
from .postgres_cluster_summary_plan import PostgresClusterSummaryPlan
from .postgres_cluster_summary_status import PostgresClusterSummaryStatus
from .postgres_database import PostgresDatabase
from .postgres_database_response import PostgresDatabaseResponse
from .postgres_endpoint import PostgresEndpoint
from .postgres_error_response import PostgresErrorResponse
from .postgres_extension import PostgresExtension
from .postgres_extension_installed_type_0 import PostgresExtensionInstalledType0
from .postgres_installed_extension import PostgresInstalledExtension
from .postgres_maintenance_window import PostgresMaintenanceWindow
from .postgres_maintenance_window_day import PostgresMaintenanceWindowDay
from .postgres_node_endpoints import PostgresNodeEndpoints
from .postgres_plan import PostgresPlan
from .postgres_plan_cpu_kind import PostgresPlanCpuKind
from .postgres_plan_plan import PostgresPlanPlan
from .postgres_query_column import PostgresQueryColumn
from .postgres_query_response import PostgresQueryResponse
from .postgres_query_response_rows_item_item import PostgresQueryResponseRowsItemItem
from .postgres_slow_query import PostgresSlowQuery
from .postgres_user import PostgresUser
from .postgres_user_credentials import PostgresUserCredentials
from .postgres_user_role import PostgresUserRole
from .process_stat import ProcessStat
from .query_postgres_database_request import QueryPostgresDatabaseRequest
from .resset_action import RessetAction
from .restore_postgres_cluster_request import RestorePostgresClusterRequest
from .root_verified_token import RootVerifiedToken
from .rotate_postgres_password_request import RotatePostgresPasswordRequest
from .rotate_postgres_password_response import RotatePostgresPasswordResponse
from .secret_key import SecretKey
from .secret_keys import SecretKeys
from .set_app_secret_request import SetAppSecretRequest
from .set_app_secret_response import SetAppSecretResponse
from .set_secretkey_request import SetSecretkeyRequest
from .set_secretkey_response import SetSecretkeyResponse
from .show_postgres_cluster_response import ShowPostgresClusterResponse
from .show_postgres_maintenance_window_response import (
    ShowPostgresMaintenanceWindowResponse,
)
from .sign_secretkey_request import SignSecretkeyRequest
from .sign_secretkey_response import SignSecretkeyResponse
from .signal_request import SignalRequest
from .signal_request_signal import SignalRequestSignal
from .start_machine_response import StartMachineResponse
from .stop_request import StopRequest
from .stop_request_signal import StopRequestSignal
from .stripped_lease import StrippedLease
from .update_machine_request import UpdateMachineRequest
from .update_metadata_request import UpdateMetadataRequest
from .update_metadata_request_metadata import UpdateMetadataRequestMetadata
from .update_postgres_maintenance_window_request import (
    UpdatePostgresMaintenanceWindowRequest,
)
from .update_postgres_maintenance_window_request_day import (
    UpdatePostgresMaintenanceWindowRequestDay,
)
from .update_postgres_user_role_request import UpdatePostgresUserRoleRequest
from .update_postgres_user_role_request_role import UpdatePostgresUserRoleRequestRole
from .update_volume_request import UpdateVolumeRequest
from .upsert_metadata_key_request import UpsertMetadataKeyRequest
from .verify_secretkey_request import VerifySecretkeyRequest
from .volume import Volume
from .volume_host_status import VolumeHostStatus
from .volume_snapshot import VolumeSnapshot
from .volume_type import VolumeType
from .wait_machine_response import WaitMachineResponse

__all__ = (
    "AcmeChallenge",
    "App",
    "AppOrganizationInfo",
    "AppSecret",
    "AppSecrets",
    "AppSecretsUpdateRequest",
    "AppSecretsUpdateRequestValues",
    "AppSecretsUpdateResp",
    "AppStatus",
    "AssignIPRequest",
    "AssignIPResponse",
    "AuthenticateTokenRequest",
    "AuthorizeResponse",
    "AuthorizeTokenRequest",
    "CertificateCheckResponse",
    "CertificateDetail",
    "CertificateEntry",
    "CertificateEntrySource",
    "CertificateEntryStatus",
    "CertificateSummary",
    "CertificateValidation",
    "CertificateValidationError",
    "CheckStatus",
    "CheckStatusStatus",
    "CreateAcmeCertificateRequest",
    "CreateAppDeployTokenRequest",
    "CreateAppDeployTokenResponse",
    "CreateAppRequest",
    "CreateAppResponse",
    "CreateCustomCertificateRequest",
    "CreateLeaseRequest",
    "CreateMachineRequest",
    "CreateOIDCTokenRequest",
    "CreatePostgresAttachmentRequest",
    "CreatePostgresAttachmentResponse",
    "CreatePostgresBackupRequest",
    "CreatePostgresBackupRequestType",
    "CreatePostgresClusterRequest",
    "CreatePostgresClusterRequestPgMajorVersion",
    "CreatePostgresClusterRequestPlan",
    "CreatePostgresClusterRequestPoolMode",
    "CreatePostgresDatabaseRequest",
    "CreatePostgresUserRequest",
    "CreatePostgresUserRequestRole",
    "CreatePostgresUserResponse",
    "CreateVolumeRequest",
    "CreateVolumeRequestFstype",
    "CurrentTokenResponse",
    "DNSRecords",
    "DNSRequirements",
    "DecryptSecretkeyRequest",
    "DecryptSecretkeyResponse",
    "DeleteAppSecretResponse",
    "DeleteSecretkeyResponse",
    "DestroyCustomCertificateResponse",
    "EnablePostgresExtensionRequest",
    "EncryptSecretkeyRequest",
    "EncryptSecretkeyResponse",
    "ErrorResponse",
    "ErrorResponseDetails",
    "ExecResponse",
    "ExtendVolumeRequest",
    "ExtendVolumeResponse",
    "FlyContainerConfig",
    "FlyContainerConfigEnv",
    "FlyContainerDependency",
    "FlyContainerDependencyCondition",
    "FlyContainerHealthcheck",
    "FlyContainerHealthcheckKind",
    "FlyContainerHealthcheckScheme",
    "FlyDNSConfig",
    "FlyDnsForwardRule",
    "FlyDnsOption",
    "FlyEnvFrom",
    "FlyEnvFromFieldRef",
    "FlyExecHealthcheck",
    "FlyFile",
    "FlyHTTPHealthcheck",
    "FlyHTTPOptions",
    "FlyHTTPResponseOptions",
    "FlyHTTPResponseOptionsHeaders",
    "FlyHTTPResponseOptionsHeadersAdditionalProperty",
    "FlyMachineCacheDrive",
    "FlyMachineCheck",
    "FlyMachineCheckKind",
    "FlyMachineConfig",
    "FlyMachineConfigChecks",
    "FlyMachineConfigEnv",
    "FlyMachineConfigMetadata",
    "FlyMachineGuest",
    "FlyMachineGuestPersistRootfs",
    "FlyMachineHTTPHeader",
    "FlyMachineInit",
    "FlyMachineMetrics",
    "FlyMachineMount",
    "FlyMachinePort",
    "FlyMachineProcess",
    "FlyMachineProcessEnv",
    "FlyMachineRestart",
    "FlyMachineRestartPolicy",
    "FlyMachineRootfs",
    "FlyMachineRootfsPersist",
    "FlyMachineSecret",
    "FlyMachineService",
    "FlyMachineServiceAutostop",
    "FlyMachineServiceCheck",
    "FlyMachineServiceConcurrency",
    "FlyMachineSpot",
    "FlyProxyProtoOptions",
    "FlyReplayCache",
    "FlyReplayCacheType",
    "FlyStatic",
    "FlyStopConfig",
    "FlyStopConfigSignal",
    "FlyTCPHealthcheck",
    "FlyTLSOptions",
    "FlyUnhealthyPolicy",
    "FlyioAccess",
    "ForkPostgresClusterRequest",
    "ForkPostgresClusterRequestPlan",
    "GetPostgresUserCredentialsResponse",
    "IPAssignment",
    "IPAssignmentNetwork",
    "IPAssignmentType",
    "IPPair",
    "ImageRef",
    "ImageRefLabels",
    "IssuedCertificate",
    "IssuedCertificateType",
    "Lease",
    "LeaseErrorResponse",
    "LeaseErrorResponseStatus",
    "LeaseOkResponse",
    "LeaseOkResponseStatus",
    "LeaseResponse",
    "LeaseResponseStatus",
    "ListAppsResponse",
    "ListCertificatesResponse",
    "ListIPAssignmentsResponse",
    "ListPostgresActiveQueriesResponse",
    "ListPostgresBackupsResponse",
    "ListPostgresClustersResponse",
    "ListPostgresDatabasesResponse",
    "ListPostgresExtensionsResponse",
    "ListPostgresPlansResponse",
    "ListPostgresSlowQueriesResponse",
    "ListPostgresUsersResponse",
    "ListenSocket",
    "MacaroonCaveatSet",
    "MacaroonCaveatSetCaveatsItem",
    "MacaroonNonce",
    "Machine",
    "MachineEvent",
    "MachineEventRequest",
    "MachineExecRequest",
    "MachineHostStatus",
    "MachineOverviewConfig",
    "MachineOverviewConfigMetadata",
    "MachineVersion",
    "MachinesListProcessesOrder",
    "MachinesListProcessesSortBy",
    "MachinesRestartSignal",
    "MachinesShowMetadataResponse200",
    "MachinesWaitState",
    "MainGetPlacementsRequest",
    "MainGetPlacementsResponse",
    "MainMemoryResponse",
    "MainReclaimMemoryRequest",
    "MainReclaimMemoryResponse",
    "MainRegionResponse",
    "MainRegionRow",
    "MainRegionRowGeoRegion",
    "MainSetMemoryLimitRequest",
    "MainStatusCode",
    "MainTokenAccess",
    "MainTokenInfo",
    "MetadataValueResponse",
    "OkResponse",
    "OrgMachine",
    "OrgMachinesResponse",
    "OrgVolume",
    "OrgVolumeHostStatus",
    "OrgVolumeType",
    "OrgVolumesResponse",
    "OrganizationRef",
    "OwnershipVerification",
    "PlacementRegionPlacement",
    "PlacementWeights",
    "PostgresActiveQuery",
    "PostgresAttachedApp",
    "PostgresAttachment",
    "PostgresBackup",
    "PostgresBackupType",
    "PostgresCluster",
    "PostgresClusterCpuKind",
    "PostgresClusterEndpoints",
    "PostgresClusterPgMajorVersion",
    "PostgresClusterPlan",
    "PostgresClusterStatus",
    "PostgresClusterSummary",
    "PostgresClusterSummaryPlan",
    "PostgresClusterSummaryStatus",
    "PostgresDatabase",
    "PostgresDatabaseResponse",
    "PostgresEndpoint",
    "PostgresErrorResponse",
    "PostgresExtension",
    "PostgresExtensionInstalledType0",
    "PostgresInstalledExtension",
    "PostgresMaintenanceWindow",
    "PostgresMaintenanceWindowDay",
    "PostgresNodeEndpoints",
    "PostgresPlan",
    "PostgresPlanCpuKind",
    "PostgresPlanPlan",
    "PostgresQueryColumn",
    "PostgresQueryResponse",
    "PostgresQueryResponseRowsItemItem",
    "PostgresSlowQuery",
    "PostgresUser",
    "PostgresUserCredentials",
    "PostgresUserRole",
    "ProcessStat",
    "QueryPostgresDatabaseRequest",
    "RessetAction",
    "RestorePostgresClusterRequest",
    "RootVerifiedToken",
    "RotatePostgresPasswordRequest",
    "RotatePostgresPasswordResponse",
    "SecretKey",
    "SecretKeys",
    "SetAppSecretRequest",
    "SetAppSecretResponse",
    "SetSecretkeyRequest",
    "SetSecretkeyResponse",
    "ShowPostgresClusterResponse",
    "ShowPostgresMaintenanceWindowResponse",
    "SignSecretkeyRequest",
    "SignSecretkeyResponse",
    "SignalRequest",
    "SignalRequestSignal",
    "StartMachineResponse",
    "StopRequest",
    "StopRequestSignal",
    "StrippedLease",
    "UpdateMachineRequest",
    "UpdateMetadataRequest",
    "UpdateMetadataRequestMetadata",
    "UpdatePostgresMaintenanceWindowRequest",
    "UpdatePostgresMaintenanceWindowRequestDay",
    "UpdatePostgresUserRoleRequest",
    "UpdatePostgresUserRoleRequestRole",
    "UpdateVolumeRequest",
    "UpsertMetadataKeyRequest",
    "VerifySecretkeyRequest",
    "Volume",
    "VolumeHostStatus",
    "VolumeSnapshot",
    "VolumeType",
    "WaitMachineResponse",
)
