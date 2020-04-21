from . import _base
from ._base import (
    PostgresError as PostgresError,
    FatalPostgresError as FatalPostgresError,
    UnknownPostgresError as UnknownPostgresError,
    InterfaceError as InterfaceError,
    InterfaceWarning as InterfaceWarning,
    PostgresLogMessage as PostgresLogMessage,
    InternalClientError as InternalClientError,
    OutdatedSchemaCacheError as OutdatedSchemaCacheError,
    ProtocolError as ProtocolError,
)

class PostgresWarning(_base.PostgresLogMessage, Warning):
    sqlstate: str = ...

class DynamicResultSetsReturned(PostgresWarning):
    sqlstate: str = ...

class ImplicitZeroBitPadding(PostgresWarning):
    sqlstate: str = ...

class NullValueEliminatedInSetFunction(PostgresWarning):
    sqlstate: str = ...

class PrivilegeNotGranted(PostgresWarning):
    sqlstate: str = ...

class PrivilegeNotRevoked(PostgresWarning):
    sqlstate: str = ...

class StringDataRightTruncation(PostgresWarning):
    sqlstate: str = ...

class DeprecatedFeature(PostgresWarning):
    sqlstate: str = ...

class NoData(PostgresWarning):
    sqlstate: str = ...

class NoAdditionalDynamicResultSetsReturned(NoData):
    sqlstate: str = ...

class SQLStatementNotYetCompleteError(_base.PostgresError):
    sqlstate: str = ...

class PostgresConnectionError(_base.PostgresError):
    sqlstate: str = ...

class ConnectionDoesNotExistError(PostgresConnectionError):
    sqlstate: str = ...

class ConnectionFailureError(PostgresConnectionError):
    sqlstate: str = ...

class ClientCannotConnectError(PostgresConnectionError):
    sqlstate: str = ...

class ConnectionRejectionError(PostgresConnectionError):
    sqlstate: str = ...

class TransactionResolutionUnknownError(PostgresConnectionError):
    sqlstate: str = ...

class ProtocolViolationError(PostgresConnectionError):
    sqlstate: str = ...

class TriggeredActionError(_base.PostgresError):
    sqlstate: str = ...

class FeatureNotSupportedError(_base.PostgresError):
    sqlstate: str = ...

class InvalidCachedStatementError(FeatureNotSupportedError): ...

class InvalidTransactionInitiationError(_base.PostgresError):
    sqlstate: str = ...

class LocatorError(_base.PostgresError):
    sqlstate: str = ...

class InvalidLocatorSpecificationError(LocatorError):
    sqlstate: str = ...

class InvalidGrantorError(_base.PostgresError):
    sqlstate: str = ...

class InvalidGrantOperationError(InvalidGrantorError):
    sqlstate: str = ...

class InvalidRoleSpecificationError(_base.PostgresError):
    sqlstate: str = ...

class DiagnosticsError(_base.PostgresError):
    sqlstate: str = ...

class StackedDiagnosticsAccessedWithoutActiveHandlerError(DiagnosticsError):
    sqlstate: str = ...

class CaseNotFoundError(_base.PostgresError):
    sqlstate: str = ...

class CardinalityViolationError(_base.PostgresError):
    sqlstate: str = ...

class DataError(_base.PostgresError):
    sqlstate: str = ...

class ArraySubscriptError(DataError):
    sqlstate: str = ...

class CharacterNotInRepertoireError(DataError):
    sqlstate: str = ...

class DatetimeFieldOverflowError(DataError):
    sqlstate: str = ...

class DivisionByZeroError(DataError):
    sqlstate: str = ...

class ErrorInAssignmentError(DataError):
    sqlstate: str = ...

class EscapeCharacterConflictError(DataError):
    sqlstate: str = ...

class IndicatorOverflowError(DataError):
    sqlstate: str = ...

class IntervalFieldOverflowError(DataError):
    sqlstate: str = ...

class InvalidArgumentForLogarithmError(DataError):
    sqlstate: str = ...

class InvalidArgumentForNtileFunctionError(DataError):
    sqlstate: str = ...

class InvalidArgumentForNthValueFunctionError(DataError):
    sqlstate: str = ...

class InvalidArgumentForPowerFunctionError(DataError):
    sqlstate: str = ...

class InvalidArgumentForWidthBucketFunctionError(DataError):
    sqlstate: str = ...

class InvalidCharacterValueForCastError(DataError):
    sqlstate: str = ...

class InvalidDatetimeFormatError(DataError):
    sqlstate: str = ...

class InvalidEscapeCharacterError(DataError):
    sqlstate: str = ...

class InvalidEscapeOctetError(DataError):
    sqlstate: str = ...

class InvalidEscapeSequenceError(DataError):
    sqlstate: str = ...

class NonstandardUseOfEscapeCharacterError(DataError):
    sqlstate: str = ...

class InvalidIndicatorParameterValueError(DataError):
    sqlstate: str = ...

class InvalidParameterValueError(DataError):
    sqlstate: str = ...

class InvalidPrecedingOrFollowingSizeError(DataError):
    sqlstate: str = ...

class InvalidRegularExpressionError(DataError):
    sqlstate: str = ...

class InvalidRowCountInLimitClauseError(DataError):
    sqlstate: str = ...

class InvalidRowCountInResultOffsetClauseError(DataError):
    sqlstate: str = ...

class InvalidTablesampleArgumentError(DataError):
    sqlstate: str = ...

class InvalidTablesampleRepeatError(DataError):
    sqlstate: str = ...

class InvalidTimeZoneDisplacementValueError(DataError):
    sqlstate: str = ...

class InvalidUseOfEscapeCharacterError(DataError):
    sqlstate: str = ...

class MostSpecificTypeMismatchError(DataError):
    sqlstate: str = ...

class NullValueNotAllowedError(DataError):
    sqlstate: str = ...

class NullValueNoIndicatorParameterError(DataError):
    sqlstate: str = ...

class NumericValueOutOfRangeError(DataError):
    sqlstate: str = ...

class SequenceGeneratorLimitExceededError(DataError):
    sqlstate: str = ...

class StringDataLengthMismatchError(DataError):
    sqlstate: str = ...

class StringDataRightTruncationError(DataError):
    sqlstate: str = ...

class SubstringError(DataError):
    sqlstate: str = ...

class TrimError(DataError):
    sqlstate: str = ...

class UnterminatedCStringError(DataError):
    sqlstate: str = ...

class ZeroLengthCharacterStringError(DataError):
    sqlstate: str = ...

class PostgresFloatingPointError(DataError):
    sqlstate: str = ...

class InvalidTextRepresentationError(DataError):
    sqlstate: str = ...

class InvalidBinaryRepresentationError(DataError):
    sqlstate: str = ...

class BadCopyFileFormatError(DataError):
    sqlstate: str = ...

class UntranslatableCharacterError(DataError):
    sqlstate: str = ...

class NotAnXmlDocumentError(DataError):
    sqlstate: str = ...

class InvalidXmlDocumentError(DataError):
    sqlstate: str = ...

class InvalidXmlContentError(DataError):
    sqlstate: str = ...

class InvalidXmlCommentError(DataError):
    sqlstate: str = ...

class InvalidXmlProcessingInstructionError(DataError):
    sqlstate: str = ...

class DuplicateJsonObjectKeyValueError(DataError):
    sqlstate: str = ...

class InvalidJsonTextError(DataError):
    sqlstate: str = ...

class InvalidSQLJsonSubscriptError(DataError):
    sqlstate: str = ...

class MoreThanOneSQLJsonItemError(DataError):
    sqlstate: str = ...

class NoSQLJsonItemError(DataError):
    sqlstate: str = ...

class NonNumericSQLJsonItemError(DataError):
    sqlstate: str = ...

class NonUniqueKeysInAJsonObjectError(DataError):
    sqlstate: str = ...

class SingletonSQLJsonItemRequiredError(DataError):
    sqlstate: str = ...

class SQLJsonArrayNotFoundError(DataError):
    sqlstate: str = ...

class SQLJsonMemberNotFoundError(DataError):
    sqlstate: str = ...

class SQLJsonNumberNotFoundError(DataError):
    sqlstate: str = ...

class SQLJsonObjectNotFoundError(DataError):
    sqlstate: str = ...

class TooManyJsonArrayElementsError(DataError):
    sqlstate: str = ...

class TooManyJsonObjectMembersError(DataError):
    sqlstate: str = ...

class SQLJsonScalarRequiredError(DataError):
    sqlstate: str = ...

class IntegrityConstraintViolationError(_base.PostgresError):
    sqlstate: str = ...

class RestrictViolationError(IntegrityConstraintViolationError):
    sqlstate: str = ...

class NotNullViolationError(IntegrityConstraintViolationError):
    sqlstate: str = ...

class ForeignKeyViolationError(IntegrityConstraintViolationError):
    sqlstate: str = ...

class UniqueViolationError(IntegrityConstraintViolationError):
    sqlstate: str = ...

class CheckViolationError(IntegrityConstraintViolationError):
    sqlstate: str = ...

class ExclusionViolationError(IntegrityConstraintViolationError):
    sqlstate: str = ...

class InvalidCursorStateError(_base.PostgresError):
    sqlstate: str = ...

class InvalidTransactionStateError(_base.PostgresError):
    sqlstate: str = ...

class ActiveSQLTransactionError(InvalidTransactionStateError):
    sqlstate: str = ...

class BranchTransactionAlreadyActiveError(InvalidTransactionStateError):
    sqlstate: str = ...

class HeldCursorRequiresSameIsolationLevelError(InvalidTransactionStateError):
    sqlstate: str = ...

class InappropriateAccessModeForBranchTransactionError(InvalidTransactionStateError):
    sqlstate: str = ...

class InappropriateIsolationLevelForBranchTransactionError(
    InvalidTransactionStateError
):
    sqlstate: str = ...

class NoActiveSQLTransactionForBranchTransactionError(InvalidTransactionStateError):
    sqlstate: str = ...

class ReadOnlySQLTransactionError(InvalidTransactionStateError):
    sqlstate: str = ...

class SchemaAndDataStatementMixingNotSupportedError(InvalidTransactionStateError):
    sqlstate: str = ...

class NoActiveSQLTransactionError(InvalidTransactionStateError):
    sqlstate: str = ...

class InFailedSQLTransactionError(InvalidTransactionStateError):
    sqlstate: str = ...

class IdleInTransactionSessionTimeoutError(InvalidTransactionStateError):
    sqlstate: str = ...

class InvalidSQLStatementNameError(_base.PostgresError):
    sqlstate: str = ...

class TriggeredDataChangeViolationError(_base.PostgresError):
    sqlstate: str = ...

class InvalidAuthorizationSpecificationError(_base.PostgresError):
    sqlstate: str = ...

class InvalidPasswordError(InvalidAuthorizationSpecificationError):
    sqlstate: str = ...

class DependentPrivilegeDescriptorsStillExistError(_base.PostgresError):
    sqlstate: str = ...

class DependentObjectsStillExistError(DependentPrivilegeDescriptorsStillExistError):
    sqlstate: str = ...

class InvalidTransactionTerminationError(_base.PostgresError):
    sqlstate: str = ...

class SQLRoutineError(_base.PostgresError):
    sqlstate: str = ...

class FunctionExecutedNoReturnStatementError(SQLRoutineError):
    sqlstate: str = ...

class ModifyingSQLDataNotPermittedError(SQLRoutineError):
    sqlstate: str = ...

class ProhibitedSQLStatementAttemptedError(SQLRoutineError):
    sqlstate: str = ...

class ReadingSQLDataNotPermittedError(SQLRoutineError):
    sqlstate: str = ...

class InvalidCursorNameError(_base.PostgresError):
    sqlstate: str = ...

class ExternalRoutineError(_base.PostgresError):
    sqlstate: str = ...

class ContainingSQLNotPermittedError(ExternalRoutineError):
    sqlstate: str = ...

class ModifyingExternalRoutineSQLDataNotPermittedError(ExternalRoutineError):
    sqlstate: str = ...

class ProhibitedExternalRoutineSQLStatementAttemptedError(ExternalRoutineError):
    sqlstate: str = ...

class ReadingExternalRoutineSQLDataNotPermittedError(ExternalRoutineError):
    sqlstate: str = ...

class ExternalRoutineInvocationError(_base.PostgresError):
    sqlstate: str = ...

class InvalidSqlstateReturnedError(ExternalRoutineInvocationError):
    sqlstate: str = ...

class NullValueInExternalRoutineNotAllowedError(ExternalRoutineInvocationError):
    sqlstate: str = ...

class TriggerProtocolViolatedError(ExternalRoutineInvocationError):
    sqlstate: str = ...

class SrfProtocolViolatedError(ExternalRoutineInvocationError):
    sqlstate: str = ...

class EventTriggerProtocolViolatedError(ExternalRoutineInvocationError):
    sqlstate: str = ...

class SavepointError(_base.PostgresError):
    sqlstate: str = ...

class InvalidSavepointSpecificationError(SavepointError):
    sqlstate: str = ...

class InvalidCatalogNameError(_base.PostgresError):
    sqlstate: str = ...

class InvalidSchemaNameError(_base.PostgresError):
    sqlstate: str = ...

class TransactionRollbackError(_base.PostgresError):
    sqlstate: str = ...

class TransactionIntegrityConstraintViolationError(TransactionRollbackError):
    sqlstate: str = ...

class SerializationError(TransactionRollbackError):
    sqlstate: str = ...

class StatementCompletionUnknownError(TransactionRollbackError):
    sqlstate: str = ...

class DeadlockDetectedError(TransactionRollbackError):
    sqlstate: str = ...

class SyntaxOrAccessError(_base.PostgresError):
    sqlstate: str = ...

class PostgresSyntaxError(SyntaxOrAccessError):
    sqlstate: str = ...

class InsufficientPrivilegeError(SyntaxOrAccessError):
    sqlstate: str = ...

class CannotCoerceError(SyntaxOrAccessError):
    sqlstate: str = ...

class GroupingError(SyntaxOrAccessError):
    sqlstate: str = ...

class WindowingError(SyntaxOrAccessError):
    sqlstate: str = ...

class InvalidRecursionError(SyntaxOrAccessError):
    sqlstate: str = ...

class InvalidForeignKeyError(SyntaxOrAccessError):
    sqlstate: str = ...

class InvalidNameError(SyntaxOrAccessError):
    sqlstate: str = ...

class NameTooLongError(SyntaxOrAccessError):
    sqlstate: str = ...

class ReservedNameError(SyntaxOrAccessError):
    sqlstate: str = ...

class DatatypeMismatchError(SyntaxOrAccessError):
    sqlstate: str = ...

class IndeterminateDatatypeError(SyntaxOrAccessError):
    sqlstate: str = ...

class CollationMismatchError(SyntaxOrAccessError):
    sqlstate: str = ...

class IndeterminateCollationError(SyntaxOrAccessError):
    sqlstate: str = ...

class WrongObjectTypeError(SyntaxOrAccessError):
    sqlstate: str = ...

class GeneratedAlwaysError(SyntaxOrAccessError):
    sqlstate: str = ...

class UndefinedColumnError(SyntaxOrAccessError):
    sqlstate: str = ...

class UndefinedFunctionError(SyntaxOrAccessError):
    sqlstate: str = ...

class UndefinedTableError(SyntaxOrAccessError):
    sqlstate: str = ...

class UndefinedParameterError(SyntaxOrAccessError):
    sqlstate: str = ...

class UndefinedObjectError(SyntaxOrAccessError):
    sqlstate: str = ...

class DuplicateColumnError(SyntaxOrAccessError):
    sqlstate: str = ...

class DuplicateCursorError(SyntaxOrAccessError):
    sqlstate: str = ...

class DuplicateDatabaseError(SyntaxOrAccessError):
    sqlstate: str = ...

class DuplicateFunctionError(SyntaxOrAccessError):
    sqlstate: str = ...

class DuplicatePreparedStatementError(SyntaxOrAccessError):
    sqlstate: str = ...

class DuplicateSchemaError(SyntaxOrAccessError):
    sqlstate: str = ...

class DuplicateTableError(SyntaxOrAccessError):
    sqlstate: str = ...

class DuplicateAliasError(SyntaxOrAccessError):
    sqlstate: str = ...

class DuplicateObjectError(SyntaxOrAccessError):
    sqlstate: str = ...

class AmbiguousColumnError(SyntaxOrAccessError):
    sqlstate: str = ...

class AmbiguousFunctionError(SyntaxOrAccessError):
    sqlstate: str = ...

class AmbiguousParameterError(SyntaxOrAccessError):
    sqlstate: str = ...

class AmbiguousAliasError(SyntaxOrAccessError):
    sqlstate: str = ...

class InvalidColumnReferenceError(SyntaxOrAccessError):
    sqlstate: str = ...

class InvalidColumnDefinitionError(SyntaxOrAccessError):
    sqlstate: str = ...

class InvalidCursorDefinitionError(SyntaxOrAccessError):
    sqlstate: str = ...

class InvalidDatabaseDefinitionError(SyntaxOrAccessError):
    sqlstate: str = ...

class InvalidFunctionDefinitionError(SyntaxOrAccessError):
    sqlstate: str = ...

class InvalidPreparedStatementDefinitionError(SyntaxOrAccessError):
    sqlstate: str = ...

class InvalidSchemaDefinitionError(SyntaxOrAccessError):
    sqlstate: str = ...

class InvalidTableDefinitionError(SyntaxOrAccessError):
    sqlstate: str = ...

class InvalidObjectDefinitionError(SyntaxOrAccessError):
    sqlstate: str = ...

class WithCheckOptionViolationError(_base.PostgresError):
    sqlstate: str = ...

class InsufficientResourcesError(_base.PostgresError):
    sqlstate: str = ...

class DiskFullError(InsufficientResourcesError):
    sqlstate: str = ...

class OutOfMemoryError(InsufficientResourcesError):
    sqlstate: str = ...

class TooManyConnectionsError(InsufficientResourcesError):
    sqlstate: str = ...

class ConfigurationLimitExceededError(InsufficientResourcesError):
    sqlstate: str = ...

class ProgramLimitExceededError(_base.PostgresError):
    sqlstate: str = ...

class StatementTooComplexError(ProgramLimitExceededError):
    sqlstate: str = ...

class TooManyColumnsError(ProgramLimitExceededError):
    sqlstate: str = ...

class TooManyArgumentsError(ProgramLimitExceededError):
    sqlstate: str = ...

class ObjectNotInPrerequisiteStateError(_base.PostgresError):
    sqlstate: str = ...

class ObjectInUseError(ObjectNotInPrerequisiteStateError):
    sqlstate: str = ...

class CantChangeRuntimeParamError(ObjectNotInPrerequisiteStateError):
    sqlstate: str = ...

class LockNotAvailableError(ObjectNotInPrerequisiteStateError):
    sqlstate: str = ...

class UnsafeNewEnumValueUsageError(ObjectNotInPrerequisiteStateError):
    sqlstate: str = ...

class OperatorInterventionError(_base.PostgresError):
    sqlstate: str = ...

class QueryCanceledError(OperatorInterventionError):
    sqlstate: str = ...

class AdminShutdownError(OperatorInterventionError):
    sqlstate: str = ...

class CrashShutdownError(OperatorInterventionError):
    sqlstate: str = ...

class CannotConnectNowError(OperatorInterventionError):
    sqlstate: str = ...

class DatabaseDroppedError(OperatorInterventionError):
    sqlstate: str = ...

class PostgresSystemError(_base.PostgresError):
    sqlstate: str = ...

class PostgresIOError(PostgresSystemError):
    sqlstate: str = ...

class UndefinedFileError(PostgresSystemError):
    sqlstate: str = ...

class DuplicateFileError(PostgresSystemError):
    sqlstate: str = ...

class SnapshotTooOldError(_base.PostgresError):
    sqlstate: str = ...

class ConfigFileError(_base.PostgresError):
    sqlstate: str = ...

class LockFileExistsError(ConfigFileError):
    sqlstate: str = ...

class FDWError(_base.PostgresError):
    sqlstate: str = ...

class FDWColumnNameNotFoundError(FDWError):
    sqlstate: str = ...

class FDWDynamicParameterValueNeededError(FDWError):
    sqlstate: str = ...

class FDWFunctionSequenceError(FDWError):
    sqlstate: str = ...

class FDWInconsistentDescriptorInformationError(FDWError):
    sqlstate: str = ...

class FDWInvalidAttributeValueError(FDWError):
    sqlstate: str = ...

class FDWInvalidColumnNameError(FDWError):
    sqlstate: str = ...

class FDWInvalidColumnNumberError(FDWError):
    sqlstate: str = ...

class FDWInvalidDataTypeError(FDWError):
    sqlstate: str = ...

class FDWInvalidDataTypeDescriptorsError(FDWError):
    sqlstate: str = ...

class FDWInvalidDescriptorFieldIdentifierError(FDWError):
    sqlstate: str = ...

class FDWInvalidHandleError(FDWError):
    sqlstate: str = ...

class FDWInvalidOptionIndexError(FDWError):
    sqlstate: str = ...

class FDWInvalidOptionNameError(FDWError):
    sqlstate: str = ...

class FDWInvalidStringLengthOrBufferLengthError(FDWError):
    sqlstate: str = ...

class FDWInvalidStringFormatError(FDWError):
    sqlstate: str = ...

class FDWInvalidUseOfNullPointerError(FDWError):
    sqlstate: str = ...

class FDWTooManyHandlesError(FDWError):
    sqlstate: str = ...

class FDWOutOfMemoryError(FDWError):
    sqlstate: str = ...

class FDWNoSchemasError(FDWError):
    sqlstate: str = ...

class FDWOptionNameNotFoundError(FDWError):
    sqlstate: str = ...

class FDWReplyHandleError(FDWError):
    sqlstate: str = ...

class FDWSchemaNotFoundError(FDWError):
    sqlstate: str = ...

class FDWTableNotFoundError(FDWError):
    sqlstate: str = ...

class FDWUnableToCreateExecutionError(FDWError):
    sqlstate: str = ...

class FDWUnableToCreateReplyError(FDWError):
    sqlstate: str = ...

class FDWUnableToEstablishConnectionError(FDWError):
    sqlstate: str = ...

class PLPGSQLError(_base.PostgresError):
    sqlstate: str = ...

class RaiseError(PLPGSQLError):
    sqlstate: str = ...

class NoDataFoundError(PLPGSQLError):
    sqlstate: str = ...

class TooManyRowsError(PLPGSQLError):
    sqlstate: str = ...

class AssertError(PLPGSQLError):
    sqlstate: str = ...

class InternalServerError(_base.PostgresError):
    sqlstate: str = ...

class DataCorruptedError(InternalServerError):
    sqlstate: str = ...

class IndexCorruptedError(InternalServerError):
    sqlstate: str = ...
