def get_connector_type(dataCconnectorType):
    connector_type = {
    'CONN_PERCENT': '%',
    'CONN_STUB':'/'
    }
    return connector_type[dataCconnectorType]