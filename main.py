import sys
import pprint as pp

sys.path.insert(1, 'ci-build-tools/')

from build_tools.shared.server import *

def test_get_instance(name, counter):
	print("\n\nTesting Get Instance\n\n")	
	payload = get_instance(name, counter)
	pp.pprint(payload.raw_data)


def test_update_label_template(name, version):
	print("\n\nTesting Update label template\n\n")
	update_label_template(version, name)


def test_get_pipeline_groups():
	print("\n\nTesting Get Pipelines Groups\n\n")
	payload = get_pipeline_groups()
	pp.pprint(payload)


def test_get_pipeline_config(name):
	print("\n\nTesting Get Pipeline Config\n\n")
	body, etag = get_pipeline_config(name)
	pp.pprint(body)
	pp.pprint(etag)


def test_edit_pipeline_config(name, config, etag):
	print("\n\nTesting Edit Pipeline Config\n\n")
	edit_pipeline_config(name, config, etag)

if __name__ == "__main__":
	print("*Collecting server data*")
	server = get_server()
	print("Done!")
	
	test_get_instance("TestSecret", 15)
	test_update_label_template("TestSecret", "1.0.1")
	test_get_pipeline_groups()
	# test_edit_pipeline_config("TestSecret", body, etag)
	test_get_pipeline_config("TestSecret")
