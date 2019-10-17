from .version import version as __version__

__all__ = (
    "get_migration",
    "migrate_data",
)

from .strategies import migrate_data, get_migration


# def create_core_migrations():
#     """Add pre-defined core migrations data files"""
#     Migration("biosphere-2-3-categories").write(
#         get_biosphere_2_3_category_migration_data(),
#         "Change biosphere category and subcategory labels to ecoinvent version 3"
#     )
#     Migration("biosphere-2-3-names").write(
#         get_biosphere_2_3_name_migration_data(),
#         "Change biosphere flow names to ecoinvent version 3"
#     )
#     Migration("simapro-ecoinvent-3.1").write(
#         get_simapro_ecoinvent_3_migration_data("3.1"),
#         "Change SimaPro names from ecoinvent 3.1 to ecoinvent names"
#     )
#     Migration("simapro-ecoinvent-3.2").write(
#         get_simapro_ecoinvent_3_migration_data("3.2"),
#         "Change SimaPro names from ecoinvent 3.2 to ecoinvent names"
#     )
#     Migration("simapro-ecoinvent-3.3").write(
#         get_simapro_ecoinvent_3_migration_data("3.3"),
#         "Change SimaPro names from ecoinvent 3.3 to ecoinvent names"
#     )
#     Migration("simapro-water").write(
#         get_simapro_water_migration_data(),
#         "Change SimaPro water flows to more standard names"
#     )
#     Migration("us-lci").write(
#         get_us_lci_migration_data(),
#         "Fix names in US LCI database"
#     )
#     Migration("default-units").write(
#         get_default_units_migration_data(),
#         "Convert to default units"
#     )
#     Migration("unusual-units").write(
#         get_unusual_units_migration_data(),
#         "Convert non-Ecoinvent units"
#     )
#     Migration("exiobase-biosphere").write(
#         get_exiobase_biosphere_migration_data(),
#         "Change biosphere flow names to ecoinvent version 3"
#     )
#     Migration("fix-ecoinvent-flows-pre-35").write(
#         get_ecoinvent_pre35_migration_data(),
#         "Update new biosphere UUIDs in Consequential 3.4"
#     )
