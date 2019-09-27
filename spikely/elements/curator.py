# Python
import inspect
import os
import shutil
import copy
from pathlib import Path
# PyQt
import PyQt5.QtGui as qg
import pkg_resources
# spikely
from . import spike_element as sp_spe
import spikeextractors as se
import spiketoolkit as st


class Curator(sp_spe.SpikeElement):
    @staticmethod
    def get_installed_spif_cls_list():
        return st.curation.installed_curation_list

    def __init__(self, spif_class):
        super().__init__(spif_class)

        self._display_name = spif_class.__name__
        self._display_icon = qg.QIcon(
            pkg_resources.resource_filename(
                'spikely.resources', 'curator.png'))
        self.param_list = copy.deepcopy(spif_class.curator_gui_params)

    @property
    def display_name(self):
        return self._display_name

    @property
    def display_icon(self):
        return self._display_icon

    def run(self, payload, next_element):

        sorting_list = payload[0]
        output_folder_str = payload[1]
        recording = payload[2]

        curated_sorting_list = []
        for i, sorting in enumerate(sorting_list):
            params_dict = {}
            params_dict['sorting'] = sorting

            if 'recording' in \
                    inspect.signature(self.spif_class).parameters:
                params_dict['recording'] = recording
            elif 'sampling_frequency' in \
                    inspect.signature(self.spif_class).parameters:
                params_dict['sampling_frequency'] = \
                    recording.get_sampling_frequency()

            for param in self.param_list:
                param_name = param['name']
                param_value = param['value']
                params_dict[param_name] = param_value

            curated_sorting = self.spif_class(**params_dict)
            curated_sorting_list.append(curated_sorting)

            if not next_element:
                print("No Exporter chosen. Defaulting to the .npz format.")
                output_folder_str_new = output_folder_str + '_curated'
                output_folder = Path(output_folder_str_new).absolute()

                if output_folder.is_dir():
                    shutil.rmtree(output_folder)
                output_folder.mkdir()

                if len(sorting_list) == 1:
                    curated_output_folder = output_folder
                else:
                    curated_output_folder = output_folder / str(i)

                if curated_output_folder.is_dir():
                    shutil.rmtree(curated_output_folder)
                os.makedirs(str(curated_output_folder))

                se.NpzSortingExtractor.write_sorting(curated_sorting,
                    curated_output_folder / 'curated_output.npz')  # noqa: E128
                print("Saved curated results to " + str(curated_output_folder))

        return curated_sorting_list, output_folder_str, recording
