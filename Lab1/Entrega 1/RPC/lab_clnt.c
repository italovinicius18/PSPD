/*
 * Please do not edit this file.
 * It was generated using rpcgen.
 */

#include <memory.h> /* for memset */
#include "lab.h"

/* Default timeout can be changed using clnt_control() */
static struct timeval TIMEOUT = { 25, 0 };

valor *
acharvalores_110011(operandos *argp, CLIENT *clnt)
{
	static valor clnt_res;

	memset((char *)&clnt_res, 0, sizeof(clnt_res));
	if (clnt_call (clnt, acharValores,
		(xdrproc_t) xdr_operandos, (caddr_t) argp,
		(xdrproc_t) xdr_valor, (caddr_t) &clnt_res,
		TIMEOUT) != RPC_SUCCESS) {
		return (NULL);
	}
	return (&clnt_res);
}
