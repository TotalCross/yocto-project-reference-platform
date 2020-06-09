def __set_defaults_totalcross_yocto():
    set_default('DISTRO', 'oel')
    set_default('SDKMACHINE', 'x86_64')


def __after_init_totalcross_yocto():
    PLATFORM_ROOT_DIR = os.environ['PLATFORM_ROOT_DIR']

    append_layers([ os.path.join(PLATFORM_ROOT_DIR, 'sources', p) for p in
                    [
                        'meta-browser',
                        'meta-clang',
                        'meta-freescale',
                        'meta-freescale-3rdparty',
                        'meta-java',
                        'meta-openembedded/meta-networking',
                        'meta-openembedded/meta-oe',
                        'meta-openembedded/meta-python',
                        'meta-python2',
                        'meta-totalcross',
                    ]])

    # FSL EULA
    eulas.accept['meta-freescale/EULA'] = 'ACCEPT_FSL_EULA = "1"'

run_set_defaults(__set_defaults_totalcross_yocto)
run_after_init(__after_init_totalcross_yocto)
