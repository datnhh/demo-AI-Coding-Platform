using Demo;

using Xunit;

namespace Demo.Tests;

public sealed class MathUtilsTests
{
    [Fact]
    public void Min_HaiSoDuong_TraVeSoNhoHon() => Assert.Equal(3, MathUtils.Min(3, 5));

    [Fact]
    public void Min_HaiSoBangNhau_TraVeSoDo() => Assert.Equal(4, MathUtils.Min(4, 4));

    [Fact]
    public void Min_ThamSoDaoNguoc_KetQuaKhongDoi() => Assert.Equal(3, MathUtils.Min(5, 3));

    [Fact]
    public void Min_CoSoAm_KetQuaKhongNhoHon0() => Assert.Equal(0, MathUtils.Min(-5, 2));

    [Fact]
    public void Min_CaHaiSoAm_KetQuaKhongNhoHon0() => Assert.Equal(0, MathUtils.Min(-5, -2));
}
