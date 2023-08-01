import copy
import json


class SchemaTransformer:
    def read_json(self, json_file_path):
        """Read json from file"""
        # Opening JSON file
        f = open(json_file_path)

        # returns JSON object as a dictionary
        data = json.load(f)

        # Closing file
        f.close()

        return data

    # def schema_key(self, key):
    #     try:
    #         return self.mapper_obj[self.schema][self.provider][key]
    #     except:
    #         return key

    def get_input_key(self, schema_key):
        temp = self.mapper_obj[self.schema][self.provider]

        new_temp = {}
        for k, v in temp.items():
            new_temp[v] = k

        try:
            return new_temp[schema_key]
        except:
            return schema_key

    # def self.get_schema_type(self, schema_key):
    #     # todo for dict nd list
    #     try:
    #         eval(self.schema_obj[schema_key])
    #     except:
    #         str. # setting default to

    def transform(self):
        # read the schem file
        if 'json' not in self.schema:
            self.schema = self.schema + '.json'

        self.schema_obj = self.read_json('schema/' + self.schema)

        # make a copy schema_obj as ouptut obj
        self.output_obj = copy.deepcopy(self.schema_obj)

        output = {}
        for schema_key, schema_type in enumerate(self.output_obj):

            if schema_type == "str":
                input_key = self.get_input_key(schema_key)

                output[schema_key] = self.input_data[input_key]
            elif 'list' in schema_type:
                input_key = self.get_input_key(schema_key)

                output[schema_key] = self.input_data[input_key]
            elif type(schema_type) == dict:
                output[schema_key] = copy.deepcopy(self.input_data[input_key])

        return output

    def build_from_json(self, json_file_path):
        json_obj = {}
        print("-----", json_file_path)
        if not json_file_path:
            return json_obj

        self.filename = json_file_path.split('/')[-1]
        self.provider = self.filename.split('_')[0]
        self.schema = self.filename.split('_')[1]
        print("schema", self.schema)
        try:
            self.extra_keyword = filename.split('_')[2]
        except:
            self.extra_keyword = None

        self.mapper_obj = self.read_json('mapping.json')

        self.input_data = self.read_json(json_file_path)

        json_obj = self.transform()

        return json_obj