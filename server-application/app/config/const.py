# -*- coding: utf-8 -*-
#!/usr/bin/env python3
BAD_REQUEST_MSG = {"success": False,
                   "status": "400: Bad Request",
                   "message": "Formato da requisição inválido."
                   }
INTERNAL_ERROR_MSG = {"success": False,
                      "status": "500: Internal Server Error",
                      "message": "Formato interna do servidor."
                      }
NOT_ACCEPTABLE_MSG = {
    "success": False,
    "status": "406: Not Acceptable",
    "message": "Não foi possível atualizar o registro com os dados informados."
}
REGISTRY_SUCCEEDED_MSG = {
    "success": True,
    "status": "201: Created",
    "message": "Registro realizado com sucesso!"
}
UPDATE_SUCCEEDED_MSG = {
    "success": True,
    "status": "202: Accepted",
    "message": "Registro realizado com sucesso!"
}
NO_CONTENT_MSG = {
    "success": True,
    "status": "204: No Content",
    "message": "Registro removido com sucesso!"
}
