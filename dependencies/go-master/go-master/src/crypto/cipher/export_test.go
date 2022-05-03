// Copyright 2018 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package cipher

// Export internal functions for testing.
var XorBytes = xorBytes
var NewCBCGenericEncrypter = newCBCGenericEncrypter
var NewCBCGenericDecrypter = newCBCGenericDecrypter
